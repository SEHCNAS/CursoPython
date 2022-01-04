def tag_bloco(texto, classe='success', inLine=False):
    tag = 'span' if inLine else 'div'
    return f'<{tag} class ="{classe}">{texto}</{tag}>'


def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco(tag_lista('Item 1', 'item 2'), 'lista'))
