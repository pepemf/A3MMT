from flask import Blueprint
from controllers.user_controller import dashboard

# Criação de um Blueprint para o módulo de usuário
user_bp = Blueprint('user_bp', __name__)

# Definição da rota e associação com a função de controle
user_bp.add_url_rule('/dashboard', view_func=dashboard, methods=['GET'])