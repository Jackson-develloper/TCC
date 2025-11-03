#!/usr/bin/env python3
import cgi
import sqlite3

print("Content-Type: text/html\n")  # Cabeçalho obrigatório

form = cgi.FieldStorage()

nome = form.getvalue("nome")
email = form.getvalue("email")
telefone = form.getvalue("telefone")
cpf = form.getvalue("cpf")
valor = form.getvalue("valor")

if not nome or not email or not valor:
    print("<h1>Erro: Preencha todos os campos obrigatórios!</h1>")
else:
    # Cria ou abre o banco de dados na mesma pasta
    conn = sqlite3.connect("doacoes.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS doacoes (
            nome TEXT,
            email TEXT,
            telefone TEXT,
            cpf TEXT,
            valor REAL
        )
    ''')
    c.execute("INSERT INTO doacoes (nome,email,telefone,cpf,valor) VALUES (?,?,?,?,?)",
              (nome, email, telefone, cpf, float(valor)))
    conn.commit()
    conn.close()

    print("<h1>Doação registrada com sucesso!</h1>")
