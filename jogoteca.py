from flask import Flask, render_template

# criar uma classe Jogo com os atributos nome, categoria, console
class Jogo():
    def __init__(self, nome, categoria, console) -> None:
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route('/')
def ola():
    j1 = Jogo('God of War', 'RPG', 'PS4')
    j2 = Jogo('Fifa', 'Esporte', 'Xbox')
    j3 = Jogo('Mortal Combate', 'Luta', 'PS2')
    lista = [j1,j2,j3]
    return render_template('lista.html',titulo='Jogos', jogos=lista)

@app.route('/novojogo')
def criar_novo_jogo():
    pass

# app.run(host='0.0.0.0', port=8080)
app.run(debug=True)