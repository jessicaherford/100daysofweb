from program import app
from flask import render_template
from datetime import datetime

timenow = datetime.today()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', time=timenow)
