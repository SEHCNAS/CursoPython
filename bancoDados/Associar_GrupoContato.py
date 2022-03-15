from mysql.connector.errors import ProgrammingError

from db import nova_conexao

Selecionar_Grupo = 'SELECT id FROM grupo where descricao = %s'
Atualizar_Contato = 'UPDATE contatos SET grupo_id = %s WHERE nome = %s '

Contato_Grupo = {
    'Michael': 'Casa',
    'Alberto': 'Trabalho',
    'Marcos': 'Casa',
    'Luana': 'Trabalho',
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in Contato_Grupo.items():
            cursor.execute(Selecionar_Grupo, (grupo,))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(Atualizar_Contato, (grupo_id, contato))
            conexao.commit()
    except ProgrammingError as error:
        print(error.msg)
    else:
        print('Contatos associados')