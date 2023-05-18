from flask import Flask
from flask_restful import Api
import BancoRest

app = Flask(__name__)
api = Api(app)

api.add_resource(BancoRest.BancoTodas, '/banco/', endpoint='bancos')
api.add_resource(BancoRest.Banco, '/banco/<id>', endpoint='banco')

if __name__ == '__main__':
    app.run(debug=True)
