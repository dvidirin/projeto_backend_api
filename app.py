from flask import Flask, render_template, request, redirect, url_for
from dados import personagens, inimigos

app = Flask(__name__)


# Rota da página principal
@app.route("/")
def index():
    return render_template("index.html")


# Rota da página de personagens
@app.route("/personagens")
def os_personagens():
    return render_template("personagens.html", personagens=personagens)


# Rota para listar os inimigos
@app.route("/inimigos")
def listar_inimigos():
    return render_template("inimigos.html", inimigos=inimigos)


# Rota para editar um inimigo
@app.route("/editar/<int:id>")
def editar_inimigo(id):
    if id in inimigos:
        inimigo = inimigos[id]
        return render_template("editar_inimigo.html", inimigo=inimigo)
    return "Inimigo não encontrado."


# Função para retornar um inimigo
def retornar_inimigo(id: int):
    if id in inimigos.keys():
        return inimigos[id]
    else:
        return {}


# Função para atualizar um inimigo
def atualizar_inimigo(id: int, dados_inimigo: dict):
    inimigos[id] = dados_inimigo


# Rota para atualizar um inimigo após a edição
@app.route("/atualizar_inimigo/<int:id>", methods=["POST"])
def atualizar_inimigo(inimigo_id):
    if request.method == "POST":
        if "salvar" in request.form:
            inimigo = {}
            inimigo["nome"] = request.form["nome"]
            inimigo["tipo"] = request.form["tipo"]
            inimigo["poder"] = request.form["poder"]
            inimigo["vida"] = request.form["vida"]

            if id in retornar_inimigo.keys():
                atualizar_inimigo(id, inimigo)

            # Redirecione de volta para a página de inimigos
            return redirect(url_for("inimigos"))
    else:
        inimigo = retornar_inimigo(id)
        inimigo["id"] = id
        return render_template("editar_inimigo.html", **inimigo)


# Rota para deletar um inimigo
@app.route("/deletar/<int:id>")
def deletar_inimigo(id):
    if id in inimigos:
        del inimigos[id]
        return redirect("/inimigos")
    return "Inimigo não encontrado."


# Rota para adicionar um novo inimigo
@app.route("/adicionar")
def adicionar_inimigo():
    return render_template("adicionar_inimigo.html")


# Rota para criar um novo inimigo
@app.route("/criar_inimigo", methods=["POST"])
def criar_inimigo():
    novo_id = max(inimigos.keys()) + 1
    novo_inimigo = {
        "nome": request.form["nome"],
        "tipo": request.form["tipo"],
        "poder": int(request.form["poder"]),
        "vida": int(request.form["vida"]),
    }
    inimigos[novo_id] = novo_inimigo
    return redirect("/inimigos")


app.run(debug=True)
