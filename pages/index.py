from components.header import el_header
from components.main import el_main
from components.footer import el_footer
from pyxhtml.core import el

def render():
    return (
        el("html",children=[
            el("head",children=[
                el("title",text="Hello world"),
                el('link',rel="stylesheet",href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css")
            ]),
            el("body",children=[
                el("div",cls="container",children=[
                    el("div",cls="row",children=[
                        el("div",cls="col-4",children=[
                            el("h1",text="hello world"),
                            el("img",src="https://media.tenor.com/3zBRB7FbwDsAAAAM/groei-it-charlottexangie.gif"),
                            el("a",text="Go to check",href="/check.html")
                        ]),
                        el("div",cls="col-4",children=[
                            el("h1",text="hello world"),
                            el("img",src="https://media.tenor.com/3zBRB7FbwDsAAAAM/groei-it-charlottexangie.gif")
                        ]),
                        el("div",cls="col-4",children=[
                            el("h1",text="hello world"),
                            el("img",src="https://media.tenor.com/3zBRB7FbwDsAAAAM/groei-it-charlottexangie.gif")
                        ])
                    ])
                ]),
                el_footer(title="Temirkhan Rustemov 12",desc="Hello world")
            ])
        ])
    )
