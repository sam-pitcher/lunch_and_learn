from flask import render_template, request
from app import app_object, union_table
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

@app_object.route('/nested_weather', methods=['GET', 'POST'])
def nested_weather():
    weather_file = 'data/nested_weather.json'
    with open(weather_file, 'r') as f:
        weather_dictionary = json.loads(f.read())

    if request.form:
        weather_type = request.form.get('weather_form')
    else:
        weather_type = ''

    print(weather_type)

    return render_template('nested_weather.html', title='Nested Weather', weather_dictionary=weather_dictionary, weather_type=weather_type)

@app_object.route('/csv_view')
def csv_view():
    view_file_array = union_table.write_view_file()
    return render_template('csv_view.html', title='CSV View', view_file_array=view_file_array)

# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#     filename = 'data.csv'
#     if request.method == 'POST':
#       f = request.files['file']
#       print(f)
#       f.save(filename)

#       # pdf_array = edit_pdf.generate_invoices('16th September', 3505, filename)
#       pdf_array = edit_pdf.generate_invoices(date_invoice_number_array[0], date_invoice_number_array[1], filename)

#     return render_template("index_pdf.html", pdf_array=pdf_array, date=str(date_invoice_number_array[0]), invoice_number=str(date_invoice_number_array[1]))


    