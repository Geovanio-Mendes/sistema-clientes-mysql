import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sua_senha_aqui",
        database="loja"
    )

def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    print("\n--- CLIENTES ---")
    for cliente in clientes:
        print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]} | CPF: {cliente[3]}")
    conexao.close()

def cadastrar_cliente():
    conexao = conectar()
    cursor = conexao.cursor()
    nome = input("Nome: ")
    email = input("Email: ")
    cpf = input("CPF: ")
    cursor.execute("INSERT INTO clientes (nome, email, cpf) VALUES (%s, %s, %s)", (nome, email, cpf))
    conexao.commit()
    print("Cliente cadastrado com sucesso!")
    conexao.close()

def buscar_cliente():
    conexao = conectar()
    cursor = conexao.cursor()
    nome = input("Digite o nome para buscar: ")
    cursor.execute("SELECT * FROM clientes WHERE nome LIKE %s", (f"%{nome}%",))
    clientes = cursor.fetchall()
    if clientes:
        for cliente in clientes:
            print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]} | {cliente[3]}")
    else:
        print("Nenhum cliente encontrado!")
    conexao.close()

def deletar_cliente():
    conexao = conectar()
    cursor = conexao.cursor()
    listar_clientes()
    id = input("\nDigite o ID do cliente para deletar: ")
    cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
    conexao.commit()
    print("Cliente deletado com sucesso!")
    conexao.close()

def atualizar_cliente():
    conexao = conectar()
    cursor = conexao.cursor()
    listar_clientes()
    id = input("\nDigite o ID do cliente para atualizar: ")
    print("O que deseja atualizar?")
    print("Nome:  1")
    print("Email: 2")
    print("CPF:   3")
    opcao = input("Escolha:")

    if opcao == "1":
        novo_nome = input("Novo nome: ")
        cursor.execute("UPDATE clientes SET nome = %s WHERE id = %s", (novo_nome, id))
    elif opcao == "2":
        novo_email = input("Novo email: ")
        cursor.execute("UPDATE clientes SET email = %s WHERE id = %s", (novo_email, id))
    elif opcao == "3":
        novo_cpf = input("Novo CPF: ")
        cursor.execute("UPDATE clientes SET CPF = %s WHERE id = %s", (novo_cpf, id))
    else:
        print("Opção inválida!")
        return

    conexao.commit()
    print("Cliente atualizado com sucesso!")
    conexao.close()

def listar_pedidos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT p.id, c.nome, p.valor_total, p.status, p.criado_em
        FROM pedidos p
        JOIN clientes c ON p.cliente_id = c.id
    """)
    pedidos = cursor.fetchall()
    print("\n--- PEDIDOS ---")
    for pedido in pedidos:
        print(f"ID: {pedido[0]} | Cliente: {pedido[1]} | Valor: R${pedido[2]} | Status: {pedido[3]}")
    conexao.close()

def cadastrar_pedido():
    conexao = conectar()
    cursor = conexao.cursor()
    listar_clientes()
    cliente_id = input("\nDigite o ID do cliente: ")
    valor = input("Valor total: R$")
    cursor.execute("INSERT INTO pedidos (cliente_id, valor_total) VALUES (%s, %s)", (cliente_id, valor))
    conexao.commit()
    print("Pedido cadastrado com sucesso!")
    conexao.close()

def atualizar_status_pedido():
    conexao = conectar()
    cursor = conexao.cursor()
    listar_pedidos()
    id = input("\nDigite o ID do pedido: ")
    print("1 - pendente")
    print("2 - aprovado")
    print("3 - cancelado")
    opcao = input("Novo status: ")
    status = {"1": "pendente", "2": "aprovado", "3": "cancelado"}
    if opcao in status:
        cursor.execute("UPDATE pedidos SET status = %s WHERE id = %s", (status[opcao], id))
        conexao.commit()
        print("Status atualizado com sucesso!")
    else:
        print("Opção inválida!")
    conexao.close()

def buscar_pedido():
    conexao = conectar()
    cursor = conexao.cursor()
    nome = input("Digite o nome do cliente para buscar: ")
    cursor.execute("""
        SELECT p.id, c.nome, p.valor_total, p.status, p.criado_em
        FROM pedidos p
        JOIN clientes c ON p.cliente_id = c.id
        WHERE c.nome LIKE %s
    """, (f"%{nome}%",))
    pedidos = cursor.fetchall()
    if pedidos:
        for pedido in pedidos:
            print(f"ID: {pedido[0]} | Cliente: {pedido[1]} | Valor: R${pedido[2]} | Status: {pedido[3]}")
    else:
        print("Nenhum pedido encontrado!")
    conexao.close()

def deletar_pedido():
    conexao = conectar()
    cursor = conexao.cursor()
    listar_pedidos()
    id = input("\nDigite o ID do pedido para deletar: ")
    cursor.execute("DELETE FROM pedidos WHERE id = %s", (id,))
    conexao.commit()
    print("Pedido deletado com sucesso!")
    conexao.close()

# Menu principal
while True:
    print("\n=== SISTEMA DE CLIENTES ===")
    print("1 - Listar clientes")
    print("2 - Cadastrar cliente")
    print("3 - Buscar cliente")
    print("4 - Deletar cliente")
    print("5 - Atualizar cliente")
    print("6 - Listar pedidos")
    print("7 - Cadastrar pedido")
    print("8 - Atualizar status do pedido")
    print("9 - Buscar pedido")
    print("10 - Deletar pedido")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        listar_clientes()
    elif opcao == "2":
        cadastrar_cliente()
    elif opcao == "3":
        buscar_cliente()
    elif opcao == "4":
        deletar_cliente()
    elif opcao == "5":
        atualizar_cliente()
    elif opcao == "6":
        listar_pedidos()
    elif opcao == "7":
        cadastrar_pedido()
    elif opcao == "8":
        atualizar_status_pedido()
    elif opcao == "9":
        buscar_pedido()
    elif opcao == "10":
        deletar_pedido()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")