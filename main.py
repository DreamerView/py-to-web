import importlib.util
import os

PAGES_DIR = "pages"
OUTPUT_DIR = "output"

def import_render_function(filepath):
    spec = importlib.util.spec_from_file_location("page_module", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.render

def save_html(html, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Сохранено: {path} {filename}")

if __name__ == "__main__":
    for file in os.listdir(PAGES_DIR):
        if file.endswith(".py"):
            page_path = os.path.join(PAGES_DIR, file)
            page_name = os.path.splitext(file)[0]
            try:
                render = import_render_function(page_path)
                html = render()
                save_html(html, f"{page_name}.html")
            except Exception as e:
                print(f"❌ Ошибка в {file}: {e}")
