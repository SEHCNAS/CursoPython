#!python3
from mysql.connector import connect

conexao = connect(
    host='localhost',
    port='3308',
    user='root',
    passwd='qwerty'
)
# onde sera mandado o codigo a ser processado no banco
cursor = conexao.cursor()
# CREATE DATABASE IF NOT EXISTS agenda
cursor.execute('CREATE DATABASE agenda')
