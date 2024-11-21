from . import db

# Definição da classe Senha que representa a tabela 'senhas' no banco de dados
class Senha(db.Model):
    __tablename__ = 'senhas'
    
    # Definição das colunas da tabela
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id', name='fk_user_id'), nullable=False)

    # Método construtor da classe
    def __init__(self, site, username, password, user_id):
        self.site = site
        self.username = username
        self.password = password
        self.user_id = user_id