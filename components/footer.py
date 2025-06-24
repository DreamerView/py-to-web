from pyxhtml.core import el

def el_footer():
    return el("footer", cls="site-footer", children=[
        el("p", text="© 2025 Temirhan. Все права защищены.")
    ])
