from config import db

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100))
    ativo = db.Column(db.Boolean())

    def __init__(self, descricao, ativo):
        self.descricao = descricao
        self.ativo = ativo

    def to_dict(self):
        return {
            'id': self.id, 
            'descricao': self.descricao,
            'ativo': self.ativo
            }

class TurmaNaoEncontrada(Exception):
    pass

def adicionar_turma(turma_data):
    nova_turma = Turma(
        descricao=turma_data['descricao'],
        ativo=turma_data['ativo']
        )
    db.session.add(nova_turma)
    db.session.commit()

def turma_por_id(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrada
    return turma.to_dict()

def listar_turmas():
    turmas = Turma.query.all()
    return [turma.to_dict() for turma in turmas]

