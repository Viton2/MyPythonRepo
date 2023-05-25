from flask import Flask
from flask_restful import Api
import aluRest

app = Flask(__name__)
api = Api(app)

api.add_resource(aluRest.AlunosRest, '/alunos', endpoint='alunos')

if __name__ == '__main__':
    app.run(debug=True)
