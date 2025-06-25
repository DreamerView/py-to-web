from py_to_web.core import el

def el_footer(**props):
    return el("footer", cls="site-footer", children=[
        el("p", text=props.get("title", "© 2025 Default Title")),
        el("span",text="hello world 12")
    ])
