from config import db

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))

    def __init__(self, nome):
        self.nome = nome

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome}

class ProfessorNaoEncontrado(Exception):
    pass

def professor_por_id(id_professor):
    prof = Professor.query.get(id_professor)
    if not prof:
        raise ProfessorNaoEncontrado
    return prof.to_dict()

def listar_professores():
    professores = Professor.query.all()
    return [professor.to_dict() for professor in professores]

def adicionar_professor(professor_data):
    novo_profesor = Professor(nome=professor_data['nome'])
    db.session.add(novo_profesor)
    db.session.commit()

def atualizar_professor(id_professor, novos_dados):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado
    professor.nome = novos_dados['nome']
    db.session.commit()

def excluir_professor(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado
    db.session.delete(professor)
    db.session.commit()