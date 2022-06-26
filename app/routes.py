from requests import request
from app import app
from flask import render_template
import os
import requests

@app.route("/login")
def login():
	print(os.getcwd())
	return render_template("login.html") 


@app.route("/index")
@app.route("/")
def index():
	print(os.getcwd())
	return render_template("index.html", content="Testing") 