
import sys
from flask import render_template, redirect, url_for, request, abort
from core import CATEGORIAS
from models.User import Users
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


from flask import redirect, render_template, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from controllers.FormController import LoginForm, RegisterForm


@login_required
def index():
	# admin = Users(email='joaopaulo@gmail.com', username='joao',password='12431')
	# db.session.add(admin)
	# db.session.commit()
	# print(Users.query.all())
	return render_template("index.html", 
		categorias=CATEGORIAS.values()
	)

def ping():
	return "<b>Pong!</b>"

def login():
	form = LoginForm()

	if form.validate_on_submit():
		user = Users.query.filter_by(email=form.email.data).first()
		
		if user:
			if user.password == form.password.data:
				login_user(user)
				return redirect(url_for("web_app.index"))

	return render_template("login.html", 
		form=form
	)

@login_required
def logout():
	logout_user()
	return redirect(url_for("web_app.login"))


def register():
	form = RegisterForm()

	if form.validate_on_submit():
		new_user = Users(email=form.email.data, username=form.username.data, password=form.password.data)
		db.session.add(new_user)
		db.session.commit()

		return redirect(url_for('web_app.login'))
	
	return render_template('register.html', form=form) 
