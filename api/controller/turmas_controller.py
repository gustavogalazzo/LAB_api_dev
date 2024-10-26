# Controllers: onde fica a lógica dos endpoints
from flask import Blueprint, jsonify, request
from api.models.turmas_model import TurmaNaoEncontrada, turma_por_id, listar_turmas, adicionar_turma, atualizar_turma, excluir_turma

turmas_bp = Blueprint('turmas', __name__)

# Rota para lista todas as turmas
@turmas_bp.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify(listar_turmas())

# Rota para listar uma turma específica
@turmas_bp.route('/turmas/<int:id_turma>', methods=['GET'])
def get_turma(id_turma):
    try:
        turma = turma_por_id(id_turma)
        return jsonify(turma)
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404
    
# Rota para criar a turma
@turmas_bp.route('/turmas', methods=['POST'])
def create_professor():
    data = request.json
    adicionar_turma(data)
    return ({'message': 'Turma criada com sucesso!'}), 201

# Rota para atualizar a turma
@turmas_bp.route('/turmas/<int:id_turma>', methods=['PUT'])
def update_turma(id_turma):
    novos_dados = request.json
    try:
        atualizar_turma(id_turma, novos_dados)
        return jsonify({'message': 'Turma atualizada com sucesso!'}), 200
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404
    
# Rota para excluir uma turma
@turmas_bp.route('/turmas/<int:id_turma>', methods=['DELETE'])
def delete_professor(id_turma):
    try:
        excluir_turma(id_turma)
        return ({'message': 'Turma deletada com sucesso!'}), 200
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404