#!python3
import mysql.connector
from mysql.connector import connect

conexao = connect(
    host='localhost',
    user='root',
    passwd='qwerty',
    port='3308'
)
# onde sera mandado o codigo a ser processado no banco
cursor = conexao.cursor()
cursor.execute('SHOW DATABASES')

for i, database in enumerate(cursor, start=1):
    print(f'Banco de dados {i}: {database[0]}')
