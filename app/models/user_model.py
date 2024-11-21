from . import db

# Definição da classe Usuario que representa a tabela 'usuarios' no banco de dados
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    # Definição das colunas da tabela
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha_mestra = db.Column(db.String(200), nullable=False)
    
    # Relacionamento com a tabela 'senhas'
    senhas = db.relationship('Senha', backref='usuario', lazy=True)