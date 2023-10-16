from flask import Flask, render_template


# dicionário de personagens

dicionario = {
    1: {
        "titulo": "Aventuras Arqueológicas",
        "nome": "Dr. David Mitchell",
        "ocupacao": "Renomado arqueólogo e historiador",
        "descricao": "Professor titular da Universidade de Oxford e diretor do Instituto de Arqueologia da universidade. Suas principais interesses de pesquisa incluem a história antiga da Grécia e Roma, bem como a arqueologia da Mesopotâmia.",
        "aparencia": "Homem alto e magro, cabelos grisalhos e olhos azuis penetrantes.",
        "personalidade": "Acadêmico brilhante, apaixonado por seu trabalho, defensor da preservação do patrimônio cultural e um homem de grande compaixão e empatia.",
        "imagem": "static\images\david\david_image.jpg",
    },
    2: {
        "titulo": "Aventuras Arqueológicas",
        "nome": "Maya",
        "ocupacao": "Jovem arqueóloga ardente e determinada",
        "descricao": "Nascida em uma pequena cidade no Brasil, estudou arqueologia na Universidade de São Paulo. Trabalhou em várias escavações de sítios arqueológicos antigos, incluindo ruínas de templos, cidades e vilas.",
        "aparencia": "Mulher de cabelos pretos e olhos castanhos, com um sorriso que ilumina uma sala.",
        "personalidade": "Apaixonada por seu trabalho, determinada a fazer contribuições significativas para o campo da arqueologia e acredita que a arqueologia pode nos ajudar a entender melhor o passado e a construir um futuro melhor.",
        "imagem": "static\images\maya\maya_image.jpg",
    },
}

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/personagens")
def os_personagens():
    return render_template("personagens.html", personagens=dicionario)


app.run(debug=True)
