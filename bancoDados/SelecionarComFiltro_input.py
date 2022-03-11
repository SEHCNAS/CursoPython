from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = "SELECT * FROM contatos where nome like %s"

with nova_conexao() as conexao:
    nome = input('Contato a localizar: ')
    args = (f'%{nome}%',)

    cursor = conexao.cursor()
    # passando as informações como argumento
    # O pacote execure protege contra sql injection
    cursor.execute(sql, args)

    for x in cursor:
        print(x)