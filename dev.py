import os
import sys
import importlib.util
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread

sys.dont_write_bytecode = True
OUTPUT_DIR = "public"

def save_html(html, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Сохранено: {path}")

def import_render_function(name):
    filepath = os.path.join("pages", f"{name}.py")
    spec = importlib.util.spec_from_file_location(name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.render

def rebuild():
    print("\n🔄 Пересборка...\n")
    pages_dir = "pages"
    for file in os.listdir(pages_dir):
        if file.endswith(".py"):
            name = os.path.splitext(file)[0]
            try:
                render = import_render_function(name)
                html = render()
                save_html(html, f"{name}.html")
            except Exception as e:
                print(f"❌ Ошибка в {file}: {e}")

def start_server(port=8000):
    def serve():
        cwd = os.getcwd()
        os.chdir(OUTPUT_DIR)
        httpd = ThreadingHTTPServer(("localhost", port), SimpleHTTPRequestHandler)
        print(f"\n🌐 Сервер доступен: http://localhost:{port}\n")
        try:
            httpd.serve_forever()
        finally:
            os.chdir(cwd)
    Thread(target=serve, daemon=True).start()

if __name__ == "__main__":
    rebuild()
    start_server()
    input("⏳ Нажмите Enter для выхода...\n")
