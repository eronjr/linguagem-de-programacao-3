from flask import Blueprint
from controllers.UsersController import getAll, get, post, delete
user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(getAll)
user_bp.route('/<int:user_id>', methods=['GET'])(get)
user_bp.route('/', methods=['POST'])(post)
user_bp.route('/<int:user_id>', methods=['DELETE'])(delete)