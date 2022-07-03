from flask import Blueprint
from controllers.PagesController import index
from controllers.PagesController import login

web_bp = Blueprint('web_app', __name__)
<<<<<<< HEAD

web_bp.route('/', methods=['GET'])(index)
web_bp.route('/index', methods=['GET'])(index)
web_bp.route('/login', methods=['GET','POST'])(login)
=======
web_bp.route('/', methods=['GET'])(index)
web_bp.route('/index', methods=['GET'])(index)
web_bp.route('/login', methods=['GET','POST'])(login)

>>>>>>> 00b16c9fc9717945f9f673a4b5c7560de23e761a
