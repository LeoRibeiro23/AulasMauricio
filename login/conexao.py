import mysql.connector
################
# Criando a conexâo
################

def conectar():
    conexao=mysql.connector.connect(
        host       =   "localhost",
        user       =   "bucefalo",
        password   =   "123456",
        database   =   "gregegay"
    )

    return conexao