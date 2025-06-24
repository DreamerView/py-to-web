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
