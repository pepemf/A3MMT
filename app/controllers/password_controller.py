import string
import random
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.password_model import Senha, db
from models.user_model import Usuario
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import os

# Criação de um Blueprint para o módulo de gerenciamento de senhas
password_bp = Blueprint('password_bp', __name__, template_folder='views', static_folder='static')

# Função para derivar uma chave a partir de uma senha e um salt
def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password)

# Função para criptografar uma senha
def encrypt_password(password, key, salt):
    backend = default_backend()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(password.encode()) + padder.finalize()
    encrypted_password = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(salt + iv + encrypted_password).decode('utf-8')

# Função para descriptografar uma senha
def decrypt_password(encrypted_password, key):
    backend = default_backend()
    encrypted_password = base64.b64decode(encrypted_password)
    salt = encrypted_password[:16]
    iv = encrypted_password[16:32]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_padded_password = decryptor.update(encrypted_password[32:]) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_password = unpadder.update(decrypted_padded_password) + unpadder.finalize()
    return decrypted_password.decode('utf-8')

# Rota para adicionar uma nova senha
@password_bp.route('/add', methods=['GET', 'POST'])
def add_password():
    if request.method == 'POST':
        site = request.form['site']
        username = request.form['username']
        password = request.form['password']
        user_id = session.get('user_id')

        if not user_id:
            flash('Você precisa estar logado para adicionar uma senha.', 'danger')