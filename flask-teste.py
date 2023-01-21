import json
import requests
from flask import Flask
from flask import render_template
from flask import request
import os

app = Flask(__name__)
# api disponivel em  http://www.omdbapi.com/apikey.aspx
# setada com secreta
api = os.environ['api_key']


@app.route('/')
def pagina():
    return render_template('pagina.html')


@app.route('/pesquisar', methods=['POST'])
def pesquisar():
    filme = request.form.get('texto')
    try:
        req = requests.get(f'http://www.omdbapi.com/?t={filme}&apikey={api}')
    except:
        return render_template('pagina.html')

    filme = json.loads(req.text)
    nome = filme['Title']
    ano = filme['Year']
    escritor = filme['Writer']
    genero = filme['Genre']
    ator = filme['Actors']
    trama = filme['Plot']
    poster = filme['Poster']
    return render_template('lista.html', nome=nome, ano=ano, escritor=escritor, genero=genero, ator=ator, trama=trama,
                           poster=poster)


app.run(host='0.0.0.0', port=81)
