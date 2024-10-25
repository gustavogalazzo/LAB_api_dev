# Controllers: onde fica a lógica dos endpoints
from flask import Blueprint, jsonify, request
from api.models.professores_model import ProfessorNaoEncontrado, professor_por_id, listar_professores, adicionar_professor, atualizar_professor, excluir_professor

professores_bp = Blueprint('professores', __name__)

@professores_bp.route('/', methods=['GET'])
def api():
    return 'A API está rodando'

# Rota para lista todos os professores
@professores_bp.route('/professores', methods=['GET'])
def get_professor():
    return jsonify(listar_professores())

# Rota para listar um professor específico
@professores_bp.route('/professores/<int:id_professor>', methods=['GET'])
def get_professor_by_id(id_professor):
    try:
        professor = professor_por_id(id_professor)
        return jsonify(professor)
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404
    
# Rota para criar o professor
@professores_bp.route('/professores', methods=['POST'])
def create_professor():
    data = request.json
    adicionar_professor(data)
    return jsonify(data), 201