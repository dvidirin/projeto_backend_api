from flask import Flask, render_template, request, redirect, url_for
import dados
from dados import personagens
import sqlite3

app = Flask(__name__)


# LEMBRE-SE ->
# Ao obter dados do servidor, a máquina do cliente usa um GET
# Ao enviar dados para o servidor, a máquina do cliente usa um POST


# Rota da página principal
@app.route("/")
def index():
    return render_template("index.html")


# Rota da página de personagens
@app.route("/personagens")
def os_personagens():
    return render_template("personagens.html", personagens=personagens)


# Rota da página dos inimigos
@app.route("/inimigos")
def listar_inimigos():
    return render_template("inimigos.html", lista_inimigos=dados.retornar_inimigos())


# Abrir um inimigo em específico (carregando seus dados) no template editar_inimigo.html
@app.route("/enemy/<int:id>", methods=["GET"])
def exibir_inimigo(id):
    id, nome, tipo, poder, vida, imagem = dados.retornar_inimigo(id)

    return render_template(
        "editar_inimigo.html",
        id=id,
        nome=nome,
        tipo=tipo,
        vida=vida,
        poder=poder,
        imagem=imagem,
    )


# NOVO com BD
# usar essa rota para ATUALIZAR, EXCLUIR e CRIAR um novo inimigo.
@app.route("/enemy/<int:id>", methods=["GET", "POST"])
def editar_inimigo(id):
    if request.method == "POST":
        if "excluir" in request.form:
            dados.remover_inimigo(id)
            return redirect(url_for("listar_inimigos"))
        elif "salvar" in request.form:
            id = request.form["id"]
            nome = request.form["nome"]
            tipo = request.form["tipo"]
            vida = request.form["vida"]
            poder = request.form["poder"]
            imagem = request.form["imagem"]

            inimigo_retornado = dados.retornar_inimigo(id)
            if inimigo_retornado:
                dados.atualizar_inimigo(
                    id=id, nome=nome, tipo=tipo, poder=poder, vida=vida, imagem=imagem
                )
            else:
                dados.criar_inimigo(
                    nome=nome, tipo=tipo, poder=poder, vida=vida, imagem=imagem
                )
            return redirect(url_for("listar_inimigos"))
    else:
        # retorna os dados de um inimigo na página de editar_inimigo
        id, nome, tipo, poder, vida, imagem = dados.retornar_inimigo(id)
        return render_template(
            "editar_inimigo.html",
            id=id,
            nome=nome,
            tipo=tipo,
            poder=poder,
            vida=vida,
            imagem=imagem,
        )


# ANTIGO com DICIONARIO
# Abrir o template editar_inimigo.html apenas com o id preenchido para permitir novo cadastro
# Dar função aos botões excluir e salvar no template editar_inimigo.html
# @app.route("/enemy/<int:id>", methods=["POST"])
# a linha acima indica que a mesma rota que já havíamos criado antes foi recriada
# #com o método POST, ou seja, quando o usuário enviar dados
# def editar_inimigo(id):
#    if "excluir" in request.form:
# Aqui estamos verificando que "excluir" está contido na requisição, ou seja
# o usuário clicou no botão excluir do formulário
#        dados.remover_inimigo(id)
#    elif "salvar" in request.form:
# Aqui estamos verificando que "salvar" está contido na requisição, ou seja,
# o usuário clicou em "salvar"
# Criando um dicionário vazio para conter os dados do inimigo que será salvo
#        inimigo = {}
# colocamos no dicionário o conteúdo que veio do formulário
#        inimigo["nome"] = request.form["nome"]
#        inimigo["tipo"] = request.form["tipo"]
#        inimigo["vida"] = request.form["vida"]
#        inimigo["poder"] = request.form["poder"]
#        inimigo["imagem"] = request.form["imagem"]
# precisa definir se vai SALVAR um novo inimigo ou ATUALIZAR um inimigo já existente
# inimigo_existente = dados.retornar_inimigo(id)
#        inimigos = dados.retornar_inimigos()
#        if id in inimigos.keys():
#            dados.atualizar_inimigo(id, inimigo)
#        else:
#            dados.criar_inimigo(**inimigo)
# vamos testar se o id do inimigo está no dicionário que contém todos eles.
# if inimigo_existente[1]:
#    inimigo["id"] = id
# caso o id já exista, vamos chamar a função atualizar_inimigo, indicando o id e os novos dados
#    dados.atualizar_inimigo(**inimigo)
# else:
# caso a id não exista, vamos chamar a função criar_inimigo passando os dados do dicionário
#    dados.criar_inimigo(**inimigo)
# o nosso return está fora dos ifs porque será executado INDEPENDENTEMENTE do botão que for clicado
#    return redirect(url_for("listar_inimigos"))


app.run(debug=True)
