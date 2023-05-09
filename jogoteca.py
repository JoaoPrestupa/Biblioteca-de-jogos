from flask import Flask, render_template, request
# LEMBRETE ** Iniciar a .venv e subir para o github


class Jogo:
    """Classe para definir os jogos"""
    def __init__(self, nome, categoria, plataforma):
        self.nome = nome
        self.categoria = categoria
        self.plataforma = plataforma


jogo1 = Jogo('Conter Strike 2', 'FPS', 'PC')
jogo2 = Jogo('Call of Duty', 'FPS', 'conso le, PC & mobile')
jogo3 = Jogo('Fifa 23', 'ESPORTES', 'Console, PC & mobile')
listajogos = [jogo1, jogo2, jogo3]


app = Flask(__name__)


@app.route('/inicio')
def chamada():
    """Funcao de chamada"""
    return render_template('lista.html', titulo='Jogos', listajogos=listajogos)


@app.route('/novo')
def novo():
    """Funcao de chamada da pagina novo"""

    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    """Funcao de chamada da pagina criar"""
    nome = request.form['nome']
    categoria = request.form['categoria']
    plataforma = request.form['plataforma']
    jogo = Jogo(nome, categoria, plataforma)
    listajogos.append(jogo)
    return render_template('lista.html', titulo='Jogos', jogos=listajogos)


app.run()
