from flask_restful import Resource, abort, reqparse

linguagens = {
    '1': {'Nome': 'Python'},
    '2': {'Nome': 'Java'},
    '3': {'Nome': 'C++'}
}


class LinguagemTodas(Resource):
    def get(self):
        return linguagens


class Linguagem(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('Nome')

    def get(self, id):
        self.senaoexiste(id)
        return linguagens[id]

    def post(self, id):
        args = self.parser.parse_args()
        print(args)
        linguagem = {'Nome': args['Nome']}
        linguagens[id] = linguagem
        return '{msg: "Linguagem Incluída"}'

    def put(self, id):
        args = self.parser.parse_args()
        linguagens[id] = {'Nome': args['Nome']}
        return '{msg: "Linguagem Alterada"}'

    def delete(self, id):
        linguagens.pop(id)
        return '{msg: "Linguagem Excluída"}'

    def senaoexiste(self, id):
        if id not in linguagens:
            abort(404, msg="Linguagem {} não existe".format(id))
