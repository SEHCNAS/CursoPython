#!python3
# instalar o connector - pip install mysql-connector
# Acessa a pasta pelo powershell e ativar o venv - .venv/Scripts/activate
# Caso necessario trocar a politica para rodar scripts -
# Set-ExecutionPolicyRemoteSigned
try:
    from mysql import connector
except ModuleNotFoundError:
    print('MySql Connector não instalado')
else:
    print('MySql connector instalado e pronto')
