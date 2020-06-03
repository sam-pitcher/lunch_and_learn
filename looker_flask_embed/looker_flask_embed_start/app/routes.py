from flask import render_template, request
from app import app_object, pbl
import json

@app_object.route('/')
@app_object.route('/index')
def index():
    return render_template('index.html', title='Homepage')

@app_object.route('/private_embed', methods=['GET', 'POST'])
def private_embed():
    return render_template('private_embed.html')

@app_object.route('/sso_embed', methods=['GET', 'POST'])
def sso_embed():
    url = pbl.generate()
    print(url)
    return render_template('sso_embed.html', url=url)

# @app_object.route('/sso_embed_formatted', methods=['GET', 'POST'])
# def sso_embed_formatted():
#     url = pbl.generate_formatted()
#     print(url)
#     return render_template('sso_embed_formatted.html', url=url)