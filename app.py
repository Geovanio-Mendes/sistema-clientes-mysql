from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route("/")
def index():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conexao.close()
    return render_template("index.html", clientes=clientes)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    email = request.form["email"]
    cpf = request.form["cpf"]
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome, email, cpf) VALUES (%s, %s, %s)", (nome, email, cpf))
    conexao.commit()
    conexao.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)