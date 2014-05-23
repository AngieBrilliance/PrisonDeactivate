# -*- coding: utf-8 -*-
from app import app
from flask import render_template

@app.route('/')
@app.route('/LandingPage')
def LandingPage():
	return render_template('LandingPage.html')

@app.route('/Login')
def Login():
	return render_template('Login.html')

@app.route('/SignUp')
def SignUp():
	return render_template('SignUp.html')
	