# app.py vai apenas inicializar a aplicação e importar os controladores.
from flask import Flask
from api.controller.faculdade_controller import professores_bp, turmas_bp, alunos_bp

app = Flask(__name__)

# Registrar os blueprints (rotas organizadas)
app.register_blueprint(professores_bp)
app.register_blueprint(turmas_bp)
app.register_blueprint(alunos_bp)

if __name__ == '__main__':
    app.run(debug=True)