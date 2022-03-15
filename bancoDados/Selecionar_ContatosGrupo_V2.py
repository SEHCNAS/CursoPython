from mysql.connector.errors import ProgrammingError
from db import nova_conexao
from collections import defaultdict

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
        try:
            cursor.execute(sql)
            contatos = cursor.fetchall()
        finally:
            cursor.close()
    except ProgrammingError as error:
        print(error.msg)
    else:
        # Agrupando os dados
        Agrupados = defaultdict(list)
        for contato in contatos:
            Agrupados[contato["grupo"]].append(contato["Nome"])
        print(Agrupados)