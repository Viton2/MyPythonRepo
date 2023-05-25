from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker


class AlunosDAO:

    def __init__(self):
        # Ligação com o esquema de banco de dados
        engine = create_engine("mysql+mysqldb://root:uniceub@localhost/db_studies?charset=utf8mb4")

        # Mapeamento Objeto Relacional com o SQLAlchemy
        DB = automap_base()
        DB.prepare(engine, reflect=True)
        self.tb_aluno = DB.classes.tb_aluno

        # Trabalho com sessões da base agora Objeto-Relacional
        session_factory = sessionmaker(bind=engine)
        self.ses = session_factory()
        # -------------------------------------------------------------------------------------------------

    def create(self, obj):
        self.ses.add(obj)
        self.ses.commit()

    def readAll(self):
        objs = self.ses.query(self.tb_aluno).all()
        return objs

    def readByIdt(self, idt):
        obj = self.ses.query(self.tb_aluno).filter_by(idt_aluno=idt).first()
        return obj

    def readByNme(self, nme):
        objs = self.ses.query(self.tb_aluno).filter(self.tb_aluno.nme_aluno.ilike('%' + nme + '%')).all()
        return objs

    def update(self):
        self.ses.commit()

    def delete(self, obj):
        self.ses.delete(obj)
        self.ses.commit()

    def getSessao(self):
        return self.ses

    def __del__(self):
        self.ses.close()
