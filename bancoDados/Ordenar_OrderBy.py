from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = "SELECT * FROM contatos Order by nome desc"
# sql = "SELECT * FROM contatos Order by nome asc"

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    print('\n'.join(registro[0] for registro in cursor))