from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import Usuario, db

# Criação de um Blueprint para o módulo de autenticação
auth_bp = Blueprint('auth_bp', __name__, template_folder='views', static_folder='static')

# Definição das rotas para redirecionamento
SIGNUP_ROUTE = 'auth_bp.signup'
USER_DASHBOARD_ROUTE = 'user_bp.dashboard'

# Rota para a página de cadastro
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Coleta de dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        senha_mestra = request.form['senha_mestra']
        confirm_senha_mestra = request.form['confirm_senha_mestra']

        # Verificação se as senhas coincidem
        if senha_mestra != confirm_senha_mestra:
            flash("As senhas mestras não coincidem.", "danger")
            return redirect(url_for(SIGNUP_ROUTE))
        
        # Geração do hash da senha
        senha_mestra_hash = generate_password_hash(senha_mestra)

        # Verificação se o email já está em uso
        usuario_existente = Usuario.query.filter_by(email=email).first()
        if usuario_existente:
            flash("Este email já está em uso.", "danger")
            return redirect(url_for(SIGNUP_ROUTE))

        # Criação de um novo usuário
        novo_usuario = Usuario(nome=nome, email=email, senha_mestra=senha_mestra_hash)
        db.session.add(novo_usuario)
        db.session.commit()

        # Armazenar o user_id na sessão
        session['user_id'] = novo_usuario.id

        # Redirecionamento para o dashboard do usuário
        return redirect(url_for(USER_DASHBOARD_ROUTE))

    # Renderização do template de cadastro
    return render_template('signup.html')

# Rota para a página de login
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Coleta de dados do formulário
        email = request.form['email']
        senha = request.form['senha']
        
        # Verificação das credenciais do usuário
        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and check_password_hash(usuario.senha_mestra, senha):
            session['user_id'] = usuario.id
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('user_bp.dashboard'))
        
        flash('Email ou senha incorretos', 'danger')
        return redirect(url_for('auth_bp.login'))

    # Renderização do template de login
    return render_template('login.html')

# Rota para logout
@auth_bp.route('/logout')
def logout():
    # Remoção do user_id da sessão
    session.pop('user_id', None)
    flash('Você saiu da sua conta.', 'success')
    return redirect(url_for('auth_bp.login'))