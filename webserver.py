from flask import Flask, render_template, request, jsonify, url_for,redirect, send_file, make_response, abort
from flask_mail import Mail, Message
import sqlite3
import json
import random
import os
import re
from bs4 import BeautifulSoup
import requests
import os.path
from os import path
from flask_compress import Compress
from flask_caching import Cache
from flask_assets import Environment, Bundle
from werkzeug.utils import secure_filename
from collections import defaultdict
from logging import FileHandler, WARNING

cache = Cache(config={'CACHE_TYPE': 'simple'})

app = Flask(__name__)
assets = Environment(app)
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)
app.logger.addHandler(file_handler)
Compress(app)
cache.init_app(app)

@app.route('/')
def home_page():
    return render_template("firstpage.html")

@app.route('/our-team/<agent_name>')
def sakher_landing_barcode(agent_name):
    if agent_name == 'ruba-dajani':
        image_link = '/static/ruba_barcode.png'
        name = 'Ruba Al Dajani'
        number = '+971505837424'
        email = 'ruba.dajani@uhemedia.com'
    elif agent_name == 'amjad-ali':
        image_link = '/static/amjad_barcode.png'
        name = 'Amjad Al Kattan'
        number = '+971553382055'
        email = 'amjadosama@uhpae.com'
    elif agent_name == 'm-shehin':
        image_link = '/static/shehin_barcode.png'
        name = 'Mohammed Shehin'
        number = '+971525839168'
        email = 'mohammedshehin@uhpae.com'
    elif agent_name == 'rizwan-ah':
        image_link = '/static/rizwan_barcode.png'
        name = 'Rizwan Ahmad'
        number = '+971543241153'
        email = 'rizwan_ahmad@uhpae.com'
    elif agent_name == 'islam-elsayed':
        image_link = '/static/islam_barcode.png'
        name = 'Islam Elsayed'
        number = '+971588045439'
        email = 'islam_elsayed@uhemedia.com'
    else:
        return abort(404)
    return render_template('agentpage.html', image_link = image_link, name = name, number = number, email = email)

if __name__ == '__main__':
    app.run(debug=True)