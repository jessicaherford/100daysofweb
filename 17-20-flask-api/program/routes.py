import request
import json

from program import app
from flask import render_template
from datetime import datetime


timenow = datetime.today()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', time=timenow)


@app.route('/chuck')
def chuck():
    joke = request.get('https://api.chucknorris.io/jokes/random')
    data = joke.json()
    return render_template('chuck.html', chuck_joke=data['value'], chuck_image=data['icon_url'])


@app.route('/pokemon', methods=['GET', 'POST'])
def pokemons():
    pokemon = []
    if request == 'POST' and 'pokecolor' in request.form:
        color = request.form.get('pokecolor')
        pokemon = get_poke_color(color)
    return render_template('pokemon.html', pokemon=pokemon)


def get_poke_color(color):
    r = request.get('https://pokeapi.co/api/v2/pokemon-color/' + color.lower())
    pokedata = r.json()
    pokemon = []

    for i in pokedata['pokemon_species']:
        pokemon.append(i['name'])

    return pokemon
