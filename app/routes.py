from app import app
from flask import render_template
import os

@app.route("/login")
def login():
	print(os.getcwd())
	return render_template("login.html") 


@app.route("/index")
@app.route("/")
def index():
	print(os.getcwd())
	return render_template("Layout.html") 