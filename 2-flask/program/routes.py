from program import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about_page')
def about_page():
    return render_template('about_page.html')


@app.route('/pricing')
def pricing():
    return render_template('pricing.html')


