from flask_migrate import Migrate
from routes.user_bp import user_bp
from routes.web_bp import web_bp
from routes.api_bp import api_bp
from flask_bootstrap import Bootstrap4
from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models.User import db
from models.User import Users

config = app_config[app_active]

app = Flask(__name__,	
		# template_folder='templates', #index.html/login.html
		# static_folder='client/assets' #css/js
)

db = SQLAlchemy(app)

bootstrap = Bootstrap4(app)

config_name = app_active

app.secret_key = config.SECRET
app.config.from_object(app_config[config_name])
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app, db)

db.init_app(app)

migrate.init_app(app, db)

app.app_context().push()

db.create_all()

from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "web_app.login"

@login_manager.user_loader
def load_user(user_id):
	return Users.query.get(int(user_id))



#registrations; blueprints, template utilities, commands
app.register_blueprint(user_bp, url_prefix='/api/users')
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(web_bp, url_prefix='/')


print("AppWeb Iniciado")

