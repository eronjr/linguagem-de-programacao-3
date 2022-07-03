from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from read_config import ConfigMysql

sql = ConfigMysql()

app = Flask(__name__)
app.config['SECRET_KEY'] = "xxxxxxxx"

db = SQLAlchemy(app)

# configuring our database uri
# note an error here
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{username}:{password}@{server}/{database_name}".format(
		username=sql.username,
		password=sql.password,
		server=sql.server,
		database_name=sql.database_name
)

# basic model

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    @classmethod
    def find_by_id(cls, session, name):
        x = session.query(cls).filter_by(id=name).all()
        if x:
            return x[0]
        return User()


if __name__ == "__main__":
    db.create_all()
    py = Users( email='joaao', password='ou', username='joao')
    db.session.add(py)
    db.session.commit()
    print(User.query.all())

    #app.run(debug=True)
