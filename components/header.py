from py_to_web.core import el

def el_header():
    return el("header", cls="site-header", children=[
        el("h1", text="Сайт Temirhan"),
        el("nav", children=[
            el("a", text="Главная", href="#"),
            el("a", text="О нас", href="#about"),
            el("a", text="Контакты", href="#contact")
        ])
    ])
