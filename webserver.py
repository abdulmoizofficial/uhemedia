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

if __name__ == '__main__':
    app.run(debug=True)