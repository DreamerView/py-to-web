import os
import sys
import time
import importlib.util
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

sys.dont_write_bytecode = True

OUTPUT_DIR = "output"

class PyxhtmlWatcher:
    def __init__(self, watched_dirs=None, output_dir="output", port=8000):
        self.root_dir = os.getcwd()
        self.output_dir = output_dir
        self.port = port
        self.watched_dirs = watched_dirs or ["pages", "components", "public"]
        self.last_modified = {}
        self.observer = Observer()

    def save_html(self, html, filename):
        path = os.path.join(OUTPUT_DIR, filename)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ Сохранено: {path} {filename}")

    def start(self):
        self._start_server()
        print("🚀 pyxhtml dev watcher запущен. Отслеживаются изменения:")
        for path in self.watched_dirs:
            full_path = os.path.join(self.root_dir, path)
            print(f"📁 {full_path}")
            os.makedirs(full_path, exist_ok=True)
            self.observer.schedule(self._ChangeHandler(self), path=full_path, recursive=True)

        self.observer.start()
        self.rebuild()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

    def _start_server(self):
        def serve():
            cwd = os.getcwd()
            os.chdir(self.output_dir)
            handler = SimpleHTTPRequestHandler
            httpd = ThreadingHTTPServer(("localhost", self.port), handler)
            print(f"\n🌐 Сервер доступен по адресу: http://localhost:{self.port}\n")
            try:
                httpd.serve_forever()
            finally:
                os.chdir(cwd)

        Thread(target=serve, daemon=True).start()

    def rebuild(self):
        print("\n🔄 Изменения обнаружены, пересобираю...\n")
        pages_dir = os.path.join(self.root_dir, "pages")
        for file in os.listdir(pages_dir):
            if file.endswith(".py"):
                name = os.path.splitext(file)[0]
                try:
                    render = self.import_render_function(name)
                    html = render()
                    fName = f"{name}.html"
                    self.save_html(html, fName)
                except Exception as e:
                    print(f"❌ Ошибка в {file}: {e}")

    def import_render_function(self, name: str):
        filepath = os.path.join(self.root_dir, "pages", f"{name}.py")
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Файл {filepath} не найден")

        spec = importlib.util.spec_from_file_location(name, filepath)
        if spec is None or spec.loader is None:
            raise ImportError(f"Не удалось загрузить модуль из {filepath}")

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if not hasattr(module, "render"):
            raise AttributeError(f"{filepath} не содержит функцию render()")

        return module.render

    class _ChangeHandler(FileSystemEventHandler):
        def __init__(self, watcher):
            super().__init__()
            self.watcher = watcher

        def on_modified(self, event):
            if event.is_directory:
                return

            now = time.time()
            path = event.src_path

            if path in self.watcher.last_modified and now - self.watcher.last_modified[path] < 0.5:
                return

            self.watcher.last_modified[path] = now

            # Изменения в pages/*.py
            if path.endswith(".py"):
                rel_path = os.path.relpath(path, self.watcher.root_dir)
                if rel_path.startswith("pages" + os.sep):
                    name = os.path.splitext(os.path.basename(path))[0]
                    try:
                        render = self.watcher.import_render_function(name)
                        html = render()
                        fName = f"{name}.html"
                        PyxhtmlWatcher.save_html(watcher,html, fName)
                    except Exception as e:
                        print(f"❌ Ошибка в {name}.py: {e}")
                    return

            # .css, .js, .html — пересобираем всё
            if path.endswith((".css", ".js", ".html")):
                self.watcher.rebuild()


if __name__ == "__main__":
    watcher = PyxhtmlWatcher()
    watcher.start()
