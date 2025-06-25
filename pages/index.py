# pages/index.py
from components.footer import el_footer
from pyxhtml.core import el

def render():
    return el("html", children=[
        el("head", children=[
            el("title", text="Hello py-to-web"),
            el("link", rel="stylesheet", href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css")
        ]),
        el("body", children=[
            el("div", cls="container", children=[
                el("h1", text="Welcome to py-to-web!"),
                el_footer(title="Made with by Temirhan")
            ])
        ])
    ])