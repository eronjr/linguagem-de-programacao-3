from flask import Blueprint
from controllers.ApiController import indicadores_anual
from controllers.ApiController import indicadores_mensal
<<<<<<< HEAD
from controllers.ApiController import documentation
=======
>>>>>>> 00b16c9fc9717945f9f673a4b5c7560de23e761a

api_bp = Blueprint('api_app', __name__)

api_bp.route('indicadores_anual', methods=['GET'])(indicadores_anual)
api_bp.route('indicadores_mensal', methods=['GET'])(indicadores_mensal)
<<<<<<< HEAD
api_bp.route('documentation', methods=['GET'])(documentation)

=======
>>>>>>> 00b16c9fc9717945f9f673a4b5c7560de23e761a
