from flask_restful import Resource, request
from flask import jsonify
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

import dao

dados = dao.ClienteDAO()


class ClienteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = dados.tb_cliente


class ClienteRest(Resource):

    def __init__(self):
        self.campos = ['idt_cliente', 'nme_cliente', 'end_cliente', 'tel_cliente']

    def get(self):
        if request.args.get(self.campos[0]) is not None:
            obj = dados.readByIdt(request.args.get(self.campos[0]))
            sch = ClienteSchema()
            return jsonify(sch.dump(obj))
        elif request.args.get("nme_cliente") is not None:
            lista = dados.readByNme(request.args.get("nme_cliente"))
            sch = ClienteSchema(many=True)
            return jsonify(sch.dump(lista))
        else:
            lista = dados.readAll()
            sch = ClienteSchema(many=True)
            return jsonify(sch.dump(lista))

    def post(self):
        obj = dados.tb_cliente()
        for c in self.campos:
            exec('obj.{}=request.args.get("{}")'.format(c, c))
        dados.create(obj)
        return jsonify({'insert': obj.idt_cliente})

    def put(self):
        obj = dados.readByIdt(request.args.get(self.campos[0]))
        if obj is None:
            return jsonify({'update': 0})
        else:
            for c in self.campos:
                if request.args.get(c) is not None:
                    exec('obj.{}=request.args.get("{}")'.format(c, c))
            dados.update()
            return jsonify({'update': obj.idt_cliente})

    def delete(self):
        idt = request.args.get(self.campos[0])
        obj = dados.readByIdt(idt)
        if obj is None:
            return jsonify({'delete': 0})
        else:
            dados.delete(obj)
            return jsonify({'delete': idt})
