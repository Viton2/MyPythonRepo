from flask import Flask
from flask_restful import Api
import rest

app = Flask(__name__)
api = Api(app)

api.add_resource(rest.ClienteRest, '/clientes', endpoint='clientes')

if __name__ == '__main__':
   app.run(debug=True)
