from flask import Blueprint, jsonify, request
from api.models.alunos_model import AlunoNaoEncontrado, aluno_por_id, listar_alunos, adicionar_aluno, atualizar_aluno, excluir_aluno
from config import db

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(listar_alunos())

@alunos_bp.route('/alunos/<int:id_aluno>', methods=['GET'])
def get_aluno(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return jsonify(aluno)
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404
    

@alunos_bp.route('/alunos', methods=['POST'])
def create_aluno():

    data = request.json
    adicionar_aluno(data)
    return jsonify(data), 201

@alunos_bp.route('/alunos/<int:id_aluno>', methods=['PUT'])
def update_aluno(id_aluno):
    data = request.json
    try:
        atualizar_aluno(id_aluno, data)
        return jsonify(aluno_por_id(id_aluno))
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

@alunos_bp.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def delete_aluno(id_aluno):
    try:
        excluir_aluno(id_aluno)
        return '', 204
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404