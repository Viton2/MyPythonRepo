from flask_restful import Resource, abort, reqparse

bancos = {
    '1': {'Nome': 'MySQL', 'Ano': '1995'},
    '2': {'Nome': 'Oracle', 'Ano': '1978'},
    '3': {'Nome': 'Postgres', 'Ano': '1994'}
}


class BancoTodas(Resource):
    def get(self):
        return bancos


class Banco(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('Nome')
        self.parser.add_argument('Ano')

    def get(self, id):
        self.senaoexiste(id)
        return bancos[id]

    def post(self, id):
        args = self.parser.parse_args()
        print(args)
        banco = {'Nome': args['Nome'], 'Ano': args['Ano']}
        bancos[id] = banco
        return '{msg: "Linguagem Incluída"}'

    def put(self, id):
        args = self.parser.parse_args()
        bancos[id] = {'Nome': args['Nome'], 'Ano': args['Ano']}
        return '{msg: "Linguagem Alterada"}'

    def delete(self, id):
        bancos.pop(id)
        return '{msg: "Linguagem Excluída"}'

    def senaoexiste(self, id):
        if id not in bancos:
            abort(404, msg="Linguagem {} não existe".format(id))
