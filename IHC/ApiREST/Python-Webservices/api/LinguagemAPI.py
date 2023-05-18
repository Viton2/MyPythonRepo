from flask import Flask
from flask_restful import Api
import LinguagemRest

app = Flask(__name__)
api = Api(app)

api.add_resource(LinguagemRest.LinguagemTodas, '/ling/', endpoint='lings')
api.add_resource(LinguagemRest.Linguagem, '/ling/<id>', endpoint='ling')

if __name__ == '__main__':
    app.run(debug=True)
