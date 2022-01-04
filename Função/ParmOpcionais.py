def tag_bloco(texto, classe='success'):
    return f'<div class ="{classe}">{texto}</div>'


if __name__ == '__main__':
    # teste (assertions) - valida o retorno da funcao
    assert tag_bloco('Incluido com sucesso') == \
        '<div class ="success">Incluido com sucesso</div>'
    assert tag_bloco('Erro ao excluir dados', 'error') == \
        '<div class ="error">Erro ao excluir dados</div>'
