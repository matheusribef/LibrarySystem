from colorama import Cursor
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resultado')
def resultado():
    criterio = request.args.get('criterio')
    valor = request.args.get('valor')
    print('\nCritério :', criterio, '\nValor :', valor, '\n')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='biblioteca')
    if conn.is_connected():
        print('Conectado a base de dados!')

    cursor = conn.cursor()
    cursor.execute(f"SELECT categoria.categoria, colecao.id_colecao, livro.id_livro, livro.nm_livro, livro.autor FROM categoria, colecao, livro WHERE {criterio} = \"{valor}\"  and colecao.id_colecao = categoria.id_colecao and colecao.id_livro = livro.id_livro GROUP BY autor")
    print(cursor)
    dados = cursor.fetchall()
    print(dados)

    html_code ="<head><style>table {  font-family: arial, sans-serif;  border-collapse: collapse;  width: 100%;}td, th {  border: 1px solid #dddddd;  text-align: left;  padding: 8px;}</style></head>"
    html_code += "<body><table><tr> <th>Categoria</th> <th>Colecao</th> <th>ID do Livro</th>  <th>Nome do Livro</th> <th>Autor</th> </tr>"
    index = 1
    for lista in dados:
        for value in lista:
            if index == 1:
                html_code += "<tr>"
                html_code += f"<td>{value}</td>"
                index += 1
            elif index == 5:
                html_code += f"<td>{value}</td>"
                html_code += "</tr>"
                index = 1
            else:
                html_code += f"<td>{value}</td>"
                index += 1

    html_code += "</table></body>"
    return html_code

app.run()