from flask import Blueprint
from controllers.auth_controller import signup, login, logout

# Criação de um Blueprint para o módulo de autenticação
auth_bp = Blueprint('auth_bp', __name__)

# Definição das rotas e associação com as funções de controle
auth_bp.add_url_rule('/signup', view_func=signup, methods=['GET', 'POST'])
auth_bp.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
auth_bp.add_url_rule('/logout', view_func=logout, methods=['GET'])