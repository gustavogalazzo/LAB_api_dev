# Controllers: onde fica a lógica dos endpoints
from flask import Blueprint, jsonify, request
from models.faculdade import professores, turmas, alunos

faculdade_bp = Blueprint('faculdade', __name__)

@faculdade_bp.route('/', methods=['GET'])
def api():
    return 'A API está rodando'

# Rota para listar todos os professores
@faculdade_bp.route('/professores', methods=['GET'])
def listar_professores():
    return jsonify({'professores': professores})

# Rota para listar um professor específico
@faculdade_bp.route('/professor/<int:prof_id>', methods=['GET'])
def professor_id(prof_id):
    for professor in professores:
        if professor['id'] == prof_id:
            return jsonify(professor)
    return jsonify({'mensagem': 'Professor não encontrado'}), 404

# Cadastrar professor
@faculdade_bp.route('/professor', methods=['POST'])
def cadastrar_prof():
    prof = request.json
    professores.append(prof)
    return jsonify({'Professor cadastrado com sucesso!': prof}), 201

# Atualizar professor
@faculdade_bp.route('/professor/<int:prof_id>', methods=['PUT'])
def update_user(prof_id):
    for professor in professores:
        if professor['id'] == prof_id:
            prof = request.json
            professor['nome'] = prof.get('nome', professor['nome'])
            professor['idade'] = prof.get('idade', professor['idade'])
            professor['matéria'] = prof.get('matéria', professor['matéria'])
            professor['observações'] = prof.get('observações', professor['observações'])
            return jsonify({'Professor atualizado com sucesso!': prof}), 201
    return jsonify({'mensagem': 'Usuário não encontrado'}), 404

# Deletar professor
@faculdade_bp.route('/professor/<int:prof_id>', methods=['DELETE'])
def delete_user(prof_id):
    for professor in professores:
        if professor['id'] == prof_id:
            professores.remove(professor)
            return jsonify({'mensagem': 'Professor removido'})
    return jsonify({'mensagem': 'Professor não encontrado'}), 404

# Rota para listar todas as turmas
@faculdade_bp.route('/turmas', methods=['GET'])
def listar_turmas():
    return jsonify({'turmas': turmas})

# Rota para listar uma turma específica com o nome do professor
@faculdade_bp.route('/turmas/<int:id>', methods=['GET'])
def turma_por_id(id):
    for turma in turmas:
        if turma['id'] == id:
            for professor in professores:
                if professor['id'] == turma['professor_id']:
                    return jsonify({'turma': turma,'professor': {'nome': professor['nome']}})
    return jsonify({'erro': 'Turma não encontrada'}), 404

# Rota para listar um aluno específico
@faculdade_bp.route('/aluno/<int:aluno_id>', methods=['GET'])
def aluno_por_id(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            return jsonify({'informações do aluno': aluno})