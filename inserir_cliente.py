import mysql.connector

# Conectando ao MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sua_senha_aqui",
    database="loja"
)

cursor = conexao.cursor()

nome = input("Nome do cliente: ")
email = input("Email: ")
cpf = input("CPF: ")

cursor.execute("INSERT INTO clientes (nome, email, cpf) VALUES (%s, %s, %s)", (nome, email, cpf))

conexao.commit()
print("Cliente cadastrado com sucesso!")
conexao.close()