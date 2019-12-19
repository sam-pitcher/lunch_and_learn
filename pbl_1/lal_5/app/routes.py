from flask import render_template, request
from app import app_object
import json

@app_object.route('/')
@app_object.route('/index')
def index():
    user = {'name': 'Sam'}
    return render_template('index.html', title='Homepage', user=user)

@app_object.route('/weather', methods=['GET', 'POST'])
def weather():
    weather_file = 'data/weather.json'
    with open(weather_file, 'r') as f:
        weather_dictionary = json.loads(f.read())

    if request.form:
        weather_type = request.form.get('weather_form')
    else:
        weather_type = ''

    print(weather_type)

    return render_template('weather.html', title='Weather', weather_dictionary=weather_dictionary, weather_type=weather_type)