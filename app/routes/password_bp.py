from flask import Blueprint
from controllers.password_controller import add_password, list_passwords, update_password, delete_password, generate_password

# Criação de um Blueprint para o módulo de gerenciamento de senhas
password_bp = Blueprint('password_bp', __name__)

# Definição das rotas e associação com as funções de controle
password_bp.add_url_rule('/add', view_func=add_password, methods=['GET', 'POST'])
password_bp.add_url_rule('/list', view_func=list_passwords, methods=['GET'])
password_bp.add_url_rule('/update/<int:id>', view_func=update_password, methods=['GET', 'POST'])
password_bp.add_url_rule('/delete/<int:id>', view_func=delete_password, methods=['POST'])
password_bp.add_url_rule('/generate', view_func=generate_password, methods=['GET', 'POST'])