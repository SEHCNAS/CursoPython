from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = "SELECT * FROM contatos where nome like 'lu%'"

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)