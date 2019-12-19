from flask import render_template
from app import app_object
import json

@app_object.route('/')
@app_object.route('/index')
def index():
    user = {'name': 'Sam'}
    return render_template('index.html', title='Homepage', user=user)

@app_object.route('/weather')
def weather():
    weather_file = 'data/weather.json'
    with open(weather_file, 'r') as f:
        weather_dictionary = json.loads(f.read())

    return render_template('weather.html', title='Weather', weather_dictionary=weather_dictionary)