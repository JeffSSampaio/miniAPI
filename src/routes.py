from .models import Usuario
from flask import request, jsonify , Blueprint
from .extensions import db
from src.services.exchange_service import get_usd_to_brl


api = Blueprint('api', __name__)

print("Rotas carregadas")

@api.route('/api/usuarios/', methods=['GET'])    
def get_usuarios():
    usuarios = Usuario.query.all()
    lista_usuarios = [{'id': usuario.id, 'nome': usuario.nome, 'email': usuario.email} for usuario in usuarios]
    print(lista_usuarios)    
    return jsonify(lista_usuarios) 

@api.route('/api/usuarios/', methods=['POST'])
def create_usuario(): 
    dados = request.get_json(silent=True)
    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({'message': 'JSON inválido ou campos ausentes (nome, email)'}), 400
    novo_usuario = Usuario(nome=dados.get('nome',), email=dados['email'])
    db.session.add(novo_usuario)
    db.session.commit()
    resp ={'id': novo_usuario.id, 'nome': novo_usuario.nome, 'email': novo_usuario.email, 'message': 'Usuário criado com sucesso!'}
    print(novo_usuario)
    return jsonify(resp)

@api.route('/api/usuarios/<int:id>/', methods=['PUT'])
def update_usuario(id):
    dados = request.get_json()
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'message': 'Usuário não encontrado'})
    if usuario:
        usuario.nome = dados.get('nome',usuario.nome)
        usuario.email = dados.get('email',usuario.email)
        db.session.commit()
        resp = {'id': usuario.id, 'nome': usuario.nome, 'email': usuario.email, 'message': 'Usuário atualizado'}
        print(usuario)
        return jsonify(resp)
    else:
        return jsonify({'message': 'Usuário não encontrado'})

@api.route('/api/usuarios/<int:id>/', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'message': 'Usuário não encontrado'})
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        print(usuario)
        resp = {'id': usuario.id, 'nome': usuario.nome, 'message': 'Usuário deletado'}
        return jsonify(resp)
    else:
        return jsonify({'message': 'Usuário não encontrado'})

@api.route('/exchange/usd-to-brl', methods=['GET'])
def usd_to_brl():
    result = get_usd_to_brl()
    return jsonify(result)
