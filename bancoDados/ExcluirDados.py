from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = 'DELETE FROM contatos where nome = %s'

args = ('lucas',)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as error:
        print(error)
    else:
        print(f'{cursor.rowcount} registros modificado(s)')