# -*- coding: utf-8 -*-
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/LandingPage')
def newsfeed():
	return render_template('LandingPage.html')

@app.route('/LawyerLogin')
def newsfeed():
	return render_template('LawyerLogin.html')

@app.route('/SignUp')
def newsfeed():
	return render_template('SignUp.html')
	