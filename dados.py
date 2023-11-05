import sqlite3

personagens = {
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
"""
inimigos = {
    1: {
        "nome": "Inimigo 1",
        "tipo": "Zumbi",
        "poder": 5,
        "vida": 20,
        "imagem": "zumbi_image.jpg",
    },
    2: {
        "nome": "Inimigo 2",
        "tipo": "Esqueleto",
        "poder": 8,
        "vida": 15,
        "imagem": "esqueleto_image.jpg",
    },
    3: {
        "nome": "Inimigo 3",
        "tipo": "Múmia",
        "poder": 7,
        "vida": 25,
        "imagem": "mumia_image.jpg",
    },
    4: {
        "nome": "Inimigo 4",
        "tipo": "Fantasma",
        "poder": 10,
        "vida": 10,
        "imagem": "fantasma_image.jpg",
    },
}
"""

# id generator antigo
# def gerar_id():
#    id = max(inimigos.keys()) + 1
#    return id


# id generator novo
def gerar_id():
    conn = sqlite3.connect("inimigos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name='inimigo'")
    next_id = cursor.fetchone()[0]
    return next_id + 1


# create inimigo antigo
# def criar_inimigo(nome: str, tipo: str, poder: int, vida: int, imagem: str):
#    inimigos[gerar_id()] = {
#        "nome": nome,
#        "tipo": tipo,
#        "poder": poder,
#        "vida": vida,
#        "imagem": imagem,
#    }


# create inimigo novo
def criar_inimigo(nome: str, tipo: str, poder: int, vida: int, imagem: str):
    try:
        conn = sqlite3.connect("inimigos.db")
        cursor = conn.cursor()
        sql_insert = "INSERT INTO inimigo (nome_inimigo, tipo_inimigo, poder_inimigo, vida_inimigo, imagem_inimigo) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(sql_insert, (nome, tipo, poder, vida, imagem))
        id_inimigo = cursor.lastrowid
        conn.commit()
        conn.close()
        return id_inimigo
    except Exception as ex:
        print(ex)
        return 0


# update antigo
# def atualizar_inimigo(id: int, dados_inimigo: dict):
#    inimigos[id] = dados_inimigo


# update novo
# atualiza os dados de um inimigo
def atualizar_inimigo(id: int, nome, tipo, poder, vida, imagem):
    try:
        conn = sqlite3.connect("inimigos.db")
        cursor = conn.cursor()
        sql_update = "UPDATE inimigo SET nome_inimigo = ?, tipo_inimigo = ?, poder_inimigo = ?, vida_inimigo = ?, imagem_inimigo = ? WHERE id_inimigo = ?"
        cursor.execute(sql_update, (nome, tipo, poder, vida, imagem, id))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False


# delete antigo
# def remover_inimigo(id: int):
#    if id in inimigos.keys():
#        del inimigos[id]


# delete novo
def remover_inimigo(id: int):
    try:
        conn = sqlite3.connect("inimigos.db")
        cursor = conn.cursor()
        sql_delete = "DELETE FROM inimigo WHERE id_inimigo = ?"
        cursor.execute(sql_delete, (id,))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False


# read antigo
# def retornar_inimigo(id: int) -> dict:
#    if id in inimigos.keys():
#        return inimigos[id]
#    else:
#        return {}


# read novo
# retorna um único inimigo
def retornar_inimigo(id: int):
    try:
        if id == 0:
            return gerar_id(), "", "", "", "", ""
        conn = sqlite3.connect("inimigos.db")
        cursor = conn.cursor()
        sql_select = "SELECT * FROM inimigo WHERE id_inimigo = ?"
        cursor.execute(sql_select, (id,))
        id, nome, tipo, poder, vida, imagem = cursor.fetchone()
        conn.close()
        return {
            "id": id,
            "nome": nome,
            "tipo": tipo,
            "poder": poder,
            "vida": vida,
            "imagem": imagem,
        }
    except:
        return False


# read retorna todos os inimigos antigo
# def retornar_inimigos() -> dict:
#    return inimigos


# read retorna todos os inimigos novo
def retornar_inimigos():
    try:
        resultado = []
        conn = sqlite3.connect("inimigos.db")
        cursor = conn.cursor()
        sql_select = "SELECT * FROM inimigo"
        cursor.execute(sql_select)
        inimigos = cursor.fetchall()
        conn.close()
        for item in inimigos:
            inimigo = {
                "id": item[0],
                "nome": item[1],
                "tipo": item[2],
                "poder": item[3],
                "vida": item[4],
                "imagem": item[5],
            }
            resultado.append(inimigo)
        return resultado
    except:
        return False


# retorna os personagens principais
def retornar_personagens() -> dict:
    return personagens
