import sys
from flask import render_template, redirect, url_for, request, abort
from core import CATEGORIAS
from models.User import Users

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def index():
	# admin = Users(email='joaopaulo@gmail.com', username='joao',password='12431')
	# db.session.add(admin)
	# db.session.commit()
	# print(Users.query.all())
	return render_template("index.html", 
		categorias=CATEGORIAS.values()
	)


def login():
	
	if request.method == 'POST':
		form = request.form
		email = form['email']
		password = form['password']
		query = Users.find_by_email(db.session, email)
		if query.password == password:
			return render_template(
				"index.html", categorias=CATEGORIAS.values()
			)
		else:
			return render_template("login.html", message="Senha ou E-mail incorreto")
	elif request.method == 'GET':
		return render_template("login.html") 