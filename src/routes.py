from .app import app
from .models import Usuario
from flask import request, jsonify
from .extensions import db


@app.route('/api/usuarios', methods=['GET'])    
def get_usuarios():
    usuarios = Usuario.query.all()
    lista_usuarios = []
    for usuario in usuarios:
        lista_usuarios.append({
            'id': usuario.id,
            'nome': usuario.nome,
            'email': usuario.email
        })
    return jsonify(lista_usuarios) 
