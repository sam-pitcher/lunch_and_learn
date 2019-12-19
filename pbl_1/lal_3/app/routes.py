from flask import render_template
from app import app_object

@app_object.route('/')
@app_object.route('/index')
def index():
    user = {'name': 'Sam'}
    return render_template('index.html', title='Homepage', user=user)