from flask import Flask, redirect, url_for
from flask_migrate import Migrate
from models import db
from routes.auth_bp import auth_bp
from routes.user_bp import user_bp
from routes.password_bp import password_bp

# Configurações do Flask
app = Flask(__name__,
            static_folder='static',
            template_folder='views'
            )
app.config.from_object('config.Config')

# Inicializando o banco de dados
db.init_app(app)

# Inicializando migrações
migrate = Migrate(app, db)

# Registrando Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(password_bp, url_prefix='/passwords')

# Rota principal que redireciona para a página de login
@app.route('/')
def home():
    return redirect(url_for('auth_bp.login'))

# Executa a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)