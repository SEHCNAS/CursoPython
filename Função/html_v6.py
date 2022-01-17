# tags suportadas por cada bloco
bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')

# Funcao para filtrar os itens de cada tag


def flitra_atrs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"' for k, v in informados.items()
                    if k in suportados)


# funcao para criar o bloco div/span
def tag_bloco(conteudo, *args, classe='success', inLine=False, **novos_atrs):
    tag = 'span' if inLine else 'div'
    html = conteudo if not callable(
        conteudo) else conteudo(*args, **novos_atrs)
    atributos = flitra_atrs(novos_atrs, bloco_atrs)
    return f'<{tag} {atributos} class ="{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atrs):  # funcao para criar o bloco de lista
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul {flitra_atrs(novos_atrs, ul_atrs)}>{lista}</ul>'


if __name__ == '__main__':
    # Item para identificar para qual tag vai as propriedades
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista'))
