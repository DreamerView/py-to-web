from pyxhtml.core import el

def el_main():
    return el("main", cls="site-main", children=[
        el("h2", text="Добро пожаловать!"),
        el("p", text="Ты создал HTML DSL-компилятор."),
        el("button", text="Попробовать", cls="btn btn-primary")
    ])
