from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
#from data import Articles
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
import json
import sys
import requests
import os
from itertools import chain
from collections import defaultdict
from datetime import datetime, timedelta, date
app = Flask(__name__)
app.static_folder = 'static'
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'log'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

# Index
@app.route('/')
def index():
    return render_template('homeA.html')


@app.route('/homeA',  methods=['GET', 'POST'])
@is_logged_in
def datos():
        #Conexion
        return  render_template('homeA.html')

# Dashboard
@app.route('/dashboardA',  methods=['GET', 'POST'])
@is_logged_in
def dashboard():
    return  render_template('arizone.html')


if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)

# conn = pymysql.connect(host='160.153.94.164', port=3306, user='admin', passwd='9)yxhJ$)j^g4', db='marketplaces')
