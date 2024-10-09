# app.py vai apenas inicializar a aplicação e importar os controladores.
from flask import Flask
from controller.faculdade_controller import faculdade_bp

app = Flask(__name__)

# Registrar os blueprints (rotas organizadas)
app.register_blueprint(faculdade_bp)

if __name__ == '__main__':
    app.run(debug=True)