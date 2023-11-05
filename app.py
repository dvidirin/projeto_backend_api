from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    jsonify,
)
import dados
from dados import personagens
import sqlite3

app = Flask(__name__)


# Bloco principal, esse não altera
# **********************************************************************
# Rota da página principal
@app.route("/")
def index():
    return render_template("index.html")


# Rota da página de personagens
@app.route("/personagens")
def os_personagens():
    return render_template("personagens.html", personagens=personagens)


# **********************************************************************
# Alterar daqui para baixo - Integração API


# Rota para retornar todos os inimigos
@app.route("/inimigos", methods=["GET"])
def get_inimigos():
    lista_inimigos = dados.retornar_inimigos()
    return jsonify(lista_inimigos)


# Rota para retornar um único inimigo
@app.route("/inimigo/<int:id>", methods=["GET"])
def get_inimigo(id):
    inimigo = dados.retornar_inimigo(id)
    if inimigo:
        return jsonify(inimigo)
    else:
        return jsonify({"message": "Inimigo não encontrado!"}), 404


# Rota para cadastrar um novo inimigo
@app.route("/inimigo", methods=["POST"])
def post_inimigo():
    inimigo = request.json
    id_inimigo = dados.criar_inimigo(**inimigo)
    inimigo["id"] = id_inimigo
    return jsonify(inimigo), 201


# Rota para alterar um inimigo
@app.route("/inimigo/<int:id>", methods=["PUT"])
def put_inimigo(id):
    inimigo = dados.retornar_inimigo(id)
    if inimigo:
        dados_atualizados = request.json
        dados_atualizados["id"] = id
        dados.atualizar_inimigo(**dados_atualizados)
        return jsonify(dados_atualizados)
    else:
        return jsonify({"message": "Inimigo não encontrado"}), 404


# Rota para deletar um inimigo
@app.route("/inimigo/<int:id>", methods=["DELETE"])
def delete_inimigo(id):
    inimigo = dados.retornar_inimigo(id)
    if inimigo:
        dados.remover_inimigo(id)
        return jsonify({"message": "Inimigo removido com sucesso"})
    else:
        return jsonify({"message": "Inimigo não encontrado"}), 404


app.run(debug=True)
