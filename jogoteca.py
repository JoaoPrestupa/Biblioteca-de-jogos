from flask import Flask, render_template


class Jogo:
    """Classe para definir os jogos"""
    def __init__(self, nome, categoria, plataforma):
        self.nome = nome
        self.categoria = categoria
        self.plataforma = plataforma


app = Flask(__name__)


@app.route('/inicio')
def chamada():
    """Funcao de chamada"""
    jogo1 = Jogo('Conter Strike 2', 'FPS', 'PC')
    jogo2 = Jogo('Call of Duty', 'FPS', 'console, PC & mobile')
    jogo3 = Jogo('Fifa 23', 'ESPORTES', 'Console, PC & mobile')
    listajogos = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', listajogos=listajogos)


app.run()
