# from flask_migrate import Migrate
# from models.User import db
# from routes.user_bp import user_bp
# from routes.web_bp import web_bp
# from routes.api_bp import api_bp
# from flask_bootstrap import Bootstrap5
# from config import app_config, app_active
# from flask_sqlalchemy import SQLAlchemy
# from app import app

# config = app_config[app_active]
# bootstrap = Bootstrap5(app)

# config_name = app_active

# app.secret_key = config.SECRET
# app.config.from_object(app_config[config_name])
# app.config.from_pyfile('config.py')
# app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(config.APP)
# migrate = Migrate(app, db) # this
# db.init_app(app)

# #app.config.from_object('config')
# #db.init_app(app)
# #migrate = Migrate(app, db)


# app.register_blueprint(user_bp, url_prefix='/users')
# app.register_blueprint(api_bp, url_prefix='/api')
# app.register_blueprint(web_bp, url_prefix='/')


# if __name__ == '__main__':
#     app.debug = True
#     app.run()
