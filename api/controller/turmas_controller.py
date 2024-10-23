# Controllers: onde fica a lógica dos endpoints
from flask import Blueprint, jsonify, request
from api.models.turmas_model import TurmaNaoEncontrada, turma_por_id, listar_turmas

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