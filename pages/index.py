# pages/index.py
from components.footer import el_footer
from pyxhtml.core import el

def render():
    return el("html", children=[
        el("head", children=[
            el("title", text="Hello py-to-web"),
            el("link", rel="stylesheet", href="style.css")
        ]),
        el("body", children=[
            el("div", cls="container", children=[
                el("img",src="logo.png", cls="logo"),
                el("h1", text="Welcome to py-to-web!"),
                el("p",text="More info ",children=[
                    el("a",text="click here",href="https://github.com/DreamerView/py-to-web")
                ])
            ])
        ])
    ])