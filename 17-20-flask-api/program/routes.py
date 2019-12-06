import requests
import json

from program import app
from flask import render_template, request
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
def pokemon():
    pokemon = []
    if request.method == 'POST' and 'pokecolour' in request.form:
        colour = request.form.get('pokecolour')
        pokemon = get_poke_colours(colour)
    return render_template('pokemon.html',
                           pokemon=pokemon)



def get_poke_colours(colour):
    r = requests.get('https://pokeapi.co/api/v2/pokemon-color/' + colour.lower())
    pokedata = r.json()
    pokemon = []

    for i in pokedata['pokemon_species']:
        pokemon.append(i['name'])

    return pokemon