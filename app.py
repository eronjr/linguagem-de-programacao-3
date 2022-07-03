from flask_migrate import Migrate
from routes.user_bp import user_bp
from routes.web_bp import web_bp
from routes.api_bp import api_bp
from flask_bootstrap import Bootstrap5
from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models.User import db



config = app_config[app_active]

app = Flask(__name__)
db = SQLAlchemy(app)

bootstrap = Bootstrap5(app)

config_name = app_active

app.secret_key = config.SECRET
app.config.from_object(app_config[config_name])
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app, db)

db.init_app(app)

# from controllers import PagesController
from models.User import Users

migrate.init_app(app, db)

app.app_context().push()


db.create_all()

# py = Users(email='joaao', password='124',username='joaao@gmail.com')
# db.session.add(py)
# db.session.commit()

# print(Users.query.all())

#registrations; blueprints, template utilities, commands
app.register_blueprint(user_bp, url_prefix='/api/users')
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(web_bp, url_prefix='/')

print("iniciando")

def create_app(test_config=None):
	
	
	bootstrap = Bootstrap5(app)

	config_name = app_active

	app.secret_key = config.SECRET
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	db.init_app(app)
	from models import User
	Migrate(app, db)

	# db = SQLAlchemy(config.APP)
	# migrate = Migrate(app, db) # this
	# db.init_app(app)

	app.config.from_object('config')
	db.init_app(app)
	#migrate = Migrate(app, db)

	#registrations; blueprints, template utilities, commands
	# app.register_blueprint(user_bp, url_prefix='/users')
	# app.register_blueprint(api_bp, url_prefix='/api')
	# app.register_blueprint(web_bp, url_prefix='/')
	print("iniciando")
	return app

