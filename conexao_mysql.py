import mysql.connector

# Conectando ao MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sua_senha_aqui",
    database="loja"
)

cursor = conexao.cursor()

# Buscando todos os clientes
cursor.execute("SELECT * FROM clientes")

clientes = cursor.fetchall()

for cliente in clientes:
    print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}")

conexao.close()