def tag_bloco(texto, classe='success', inLine=False):
    tag = 'span' if inLine else 'div'
    return f'<{tag} class ="{classe}">{texto}</{tag}>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('Inline e classe', 'info', True))
    print(tag_bloco('inline', inLine=False))
    print(tag_bloco(inLine=True, texto='fora de ordem',
                    classe='ordem inversa'))
