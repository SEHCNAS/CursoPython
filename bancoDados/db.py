#!python3
import mysql.connector
from mysql.connector import connect
from contextlib import contextmanager

parametros = dict(
    host='localhsot',
    port=3308,
    user='root',
    passwd='qwerty',
    database='agenda'
)


@contextmanager
def nova_conexao():
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        # Fecha a conexao
        if (conexao and conexao.is_connected()):
            conexao.close()
