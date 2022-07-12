from flask import Blueprint

#controllers
from controllers.PagesController import index
from controllers.PagesController import login
from controllers.PagesController import ping
from controllers.PagesController import logout
from controllers.PagesController import register

web_bp = Blueprint('web_app', __name__)

web_bp.route('/', methods=['GET'])(index)
web_bp.route('/index', methods=['GET'])(index)
web_bp.route('/ping', methods=['GET','POST'])(ping)

#login #logout #register
web_bp.route('/login', methods=['GET','POST'])(login)
web_bp.route('/logout', methods=['GET','POST'])(logout)
web_bp.route('/register', methods=['GET','POST'])(register)