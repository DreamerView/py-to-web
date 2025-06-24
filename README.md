# ⚡ py-to-web

**py-to-web** is a minimalist Python framework that transforms simple Python files with a `render()` function into static HTML pages. It's designed for developers who value simplicity, readability, and full control over their markup.

---

## 🚀 Quick Start

```bash
git clone https://github.com/DreamerView/py-to-web.git
cd py-to-web
python dev.py
```

Then open your browser at:

```
http://localhost:8000
```

---

## 📂 Project Structure

```
py-to-web/
├── pages/             # Python files with render() -> str
│   └── index.py       # Example: returns a full HTML string
├── components/        # Reusable Python blocks
├── public/            # Static files like CSS, JS, images
├── output/            # Auto-generated HTML output
├── main.py            # Core logic to save HTML
└── dev.py             # Watcher + HTTP dev server
```

---

## 🧠 Example Page

```python
# pages/index.py
from components.header import el_header
from components.main import el_main
from components.footer import el_footer
from pyxhtml.core import el

def render():
    return (
        '<!DOCTYPE html>' +
        el("html", lang="ru", children=[
            el("head", children=[
                el("meta", charset="UTF-8"),
                el("title", text="pyxhtml Demo")
            ]),
            el("body", children=[
                el("h1",text="Nice work!!!"),
                el_header(),
                el_main(),
                el_footer()
            ])
        ])
    )

```

---

## 🔥 Features

* 📁 Renders only `.py` files inside `pages`
* ✨ Clean Python syntax, no template engines
* 🌐 Built-in local HTTP server on `localhost:8000`
* 👀 Watches changes in `pages/`, `components/`, and `public/`
* ⚡ Super fast and dependency-light (only `watchdog`)

---

## 📦 Dependencies

```bash
pip install watchdog
```

---

## 📌 Roadmap

* [ ] Nested pages support (`pages/blog/index.py`)
* [ ] Markdown rendering
* [ ] HTML minification
* [ ] CLI: `py-to-web build` and `py-to-web dev`

---

## 💡 Philosophy

> Use Python as your templating language. No abstraction, just code.

---

Made with love by Temirkhan.