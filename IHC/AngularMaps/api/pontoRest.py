from flask_restful import Resource
from flask import jsonify
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from IHC.AngularMaps.dao.dao import PontoDAO

dao = PontoDAO()


class PontoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = dao.tb_ponto


class PontoRest(Resource):

    def get(self):
        lista = dao.readAll()
        sch = PontoSchema(many=True)
        return jsonify(sch.dump(lista))
