from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = """
    SELECT 
        grupo.descricao AS grupo,
        contatos.nome AS Nome
        FROM contatos
        INNER JOIN grupo ON contatos.grupo_id = grupo.id
        ORDER BY grupo, Nome
"""

with nova_conexao() as conexao:
    try:
        # Retorna um dicionario
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as error:
        print(error.msg)
    else:
        for contato in contatos:
            print(f'{contato["grupo"]}: {contato["Nome"]}')