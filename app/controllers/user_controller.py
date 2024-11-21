from flask import Blueprint, render_template, session, redirect, url_for, flash
from models.user_model import Usuario

# Criação de um Blueprint para o módulo de usuário
user_bp = Blueprint('user_bp', __name__, template_folder='views', static_folder='static')

# Rota para o dashboard do usuário
@user_bp.route('/dashboard')
def dashboard():
    # Obtém o user_id da sessão
    user_id = session.get('user_id')
    if not user_id:
        flash('Você precisa estar logado para acessar o dashboard.', 'danger')
        return redirect(url_for('auth_bp.login'))

    # Busca o usuário no banco de dados
    usuario = Usuario.query.get(user_id)
    if not usuario:
        flash('Usuário não encontrado.', 'danger')
        return redirect(url_for('auth_bp.login'))

    # Renderiza o template do dashboard com os dados do usuário
    return render_template('dashboard.html', usuario=usuario)