import os

# Obtém o diretório base do arquivo atual
basedir = os.path.abspath(os.path.dirname(__file__))

# Classe de configuração para a aplicação Flask
class Config:
    # URI de conexão com o banco de dados SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    # Desativa o rastreamento de modificações do SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Chave secreta para a aplicação Flask
    SECRET_KEY = os.urandom(32)
    # Ativa o modo de depuração
    DEBUG = True