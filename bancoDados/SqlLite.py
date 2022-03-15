from sqlite3 import connect, ProgrammingError, Row

sql = """
    SELECT *
        FROM contatos
"""

tabela_contatos = """
    CREATE TABLE  contatos(
        nome varchar(50), 
        telefone varchar(50)
    )
"""

sql_Inserir = """
    INSERT INTO contatos (nome, telefone)
    values(?,?)
"""
args = (
    ('Maria', '1478-5236'),
    ('Alberto', '6985-1472'),
    ('Jose', '1597-3695'),
    ('Luffy', '1475-8745'),
    ('Trinity', '1457-5555'),
)

try:
    conexao = connect(':memory:')
    conexao.row_factory = Row

    cursor = conexao.cursor()
    cursor.execute(tabela_contatos)
    cursor.executemany(sql_Inserir, args)
    cursor.execute(sql)
except ProgrammingError as error:
    print(error)
else:
    for contato in cursor:
        print(contato['Nome'])
