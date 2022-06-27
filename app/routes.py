from app import app
from app import CATEGORIAS

from flask import render_template
import os

@app.route("/login")
def login():
	return render_template("login.html") 


@app.route("/index")
@app.route("/")
def index():
	return render_template("index.html", categorias=CATEGORIAS.values()) 
