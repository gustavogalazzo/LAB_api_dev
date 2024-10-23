# app.py vai apenas inicializar a aplicação e importar os controladores.
from config import app, db
from api.controller.professores_controller import professores_bp
from api.controller.turmas_controller import turmas_bp
from api.controller.alunos_controller import alunos_bp

# Registrar os blueprints (rotas organizadas)
app.register_blueprint(professores_bp)
app.register_blueprint(turmas_bp)
app.register_blueprint(alunos_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"])