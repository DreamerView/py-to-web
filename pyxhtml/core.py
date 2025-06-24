SELF_CLOSING_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img",
    "input", "link", "meta", "source", "track", "wbr"
}

def el(tag, text=None, children=None, **attrs):
    if 'cls' in attrs:
        attrs['class'] = attrs.pop('cls')

    attr_str = ''.join(f' {k}="{v}"' for k, v in attrs.items())

    if tag.lower() in SELF_CLOSING_TAGS:
        return f"<{tag}{attr_str} />"

    inner_html = str(text) if text else ''
    if children:
        if isinstance(children, (str, dict)):
            children = [children]
        for child in children:
            if isinstance(child, str):
                inner_html += child
            elif isinstance(child, dict):
                inner_html += el(**child)
            else:
                inner_html += child

    return f"<{tag}{attr_str}>{inner_html}</{tag}>"
