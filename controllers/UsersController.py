import sys
from flask import render_template, redirect, url_for, request, abort, jsonify
from models.User import Users
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import select, delete as delete_sql, values

db = SQLAlchemy()

def getAll():
    
    data = {
        'data':[
            
                {
                    'email': data.email,
                    'username': data.username,
                    'id': data.id,
                } 

                for data in Users.query.all()
            ]
    }

    return jsonify(data)
    

def get(user_id):
    query = Users.find_by_id(db.session, user_id)
    return jsonify( {
        'email':query.email,
        'username':query.username,
        'id':query.id
    })

def post():
    form = request.form
    email = form['email']
    password = form['password']
    username = form['username']
    
    data = Users(
        email=email, 
        password=password,
        username=username
    )
    
    db.session.add(data)
    db.session.commit()

    return 'ok'

def delete(user_id):
    sql = delete_sql(Users).where(Users.id == user_id)
    db.session.execute(sql)

    db.session.commit()

    return {
        'message':'deletado'
    }

def update(user_id):
    ...
