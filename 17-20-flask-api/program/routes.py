import requests
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
    joke = requests.get('https://api.chucknorris.io/jokes/random')
    data = joke.json()
    return render_template('chuck.html', chuck_joke=data['value'], chuck_image=data['icon_url'])



