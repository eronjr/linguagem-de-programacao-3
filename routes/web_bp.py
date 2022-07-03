from flask import Blueprint
from controllers.PagesController import index
from controllers.PagesController import login

web_bp = Blueprint('web_app', __name__)

web_bp.route('/', methods=['GET'])(index)
web_bp.route('/index', methods=['GET'])(index)
web_bp.route('/login', methods=['GET','POST'])(login)
