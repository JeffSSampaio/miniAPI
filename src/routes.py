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

@app.route('/api/usuarios', methods=['POST'])
def create_usuario(): 
 dados = request.get_json()
 novo_usuario = Usuario(nome=dados['nome'], email=dados['email'])
 db.session.add(novo_usuario)
 db.session.commit()
 return jsonify({f'id': novo_usuario.id, 'nome': novo_usuario.nome, 'email': novo_usuario.email, 'message': 'Usuário criado com sucesso!'})

@app.route('/api/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    dados = request.get_json()
    usuario = Usuario.query.get(id)
    if usuario:
        usuario.nome = dados['nome']
        usuario.email = dados['email']
        db.session.commit()
        return jsonify({'id': usuario.id, 'nome': usuario.nome, 'email': usuario.email, 'message': 'Usuário atualizado'})
    else:
        return jsonify({'message': 'Usuário não encontrado'})

@app.route('/api/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({'id':usuario.id, 'nome': usuario.nome  ,'message': 'Usuário deletado '})
    else:
        return jsonify({'message': 'Usuário não encontrado'})