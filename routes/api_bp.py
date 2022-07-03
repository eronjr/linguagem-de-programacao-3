from flask import Blueprint
from controllers.ApiController import indicadores_anual
from controllers.ApiController import indicadores_mensal
from controllers.ApiController import documentation

api_bp = Blueprint('api_app', __name__)

api_bp.route('indicadores_anual', methods=['GET'])(indicadores_anual)
api_bp.route('indicadores_mensal', methods=['GET'])(indicadores_mensal)
api_bp.route('documentation', methods=['GET'])(documentation)

