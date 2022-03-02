#!python3
from mysql.connector import connect

conexao = connect(
    host='localhost',
    port='3308',
    user='root',
    passwd='qwerty',
    # se realziar o pip install mysql-connector-python não precisa dessa linha
    # auth_plugin='mysql_native_password'
)

print(conexao)
