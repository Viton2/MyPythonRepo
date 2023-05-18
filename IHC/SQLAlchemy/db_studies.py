from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from datetime import timedelta

# ----- VARIÁVEIS GLOBAIS ------------------------------------
# Ligação com o esquema de banco de dados
engine = create_engine("mysql+mysqldb://root:uniceub@localhost/db_studies?charset=utf8mb4")

# Mapeamento Objeto Relacional com o SQLAlchemy
DB = automap_base()
DB.prepare(engine, reflect=True)
tb_disciplina = DB.classes.tb_disciplina
tb_aluno = DB.classes.tb_aluno
ta_matricula = DB.classes.ta_matricula

# Trabalho com sessões da base agora Objeto-Relacional
session_factory = sessionmaker(bind=engine)
ses = session_factory()
# ------------------------------------------------------------

matriculas = ses.query(ta_matricula).all()

print("Nome do Aluno | Sigla da Matéria | Carga Horária | Menção")
for a in matriculas:
    print(a.tb_aluno.nme_aluno, a.tb_disciplina.sgl_disc, a.tb_disciplina.crg_hor, a.mencao)

alunos = ses.query(tb_aluno).all()
disciplinas = ses.query(tb_disciplina).all()

# for c in disciplinas:
#     print('-' * 50)
#     print('Nome da Disciplina:', c.nme_disc)
#     print('Sigla da Disciplina:', c.sgl_disc)
#     print('Carga Horaria:', c.crg_hor)

for c in alunos:
    print('-' * 50)
    print('Nome:', c.nme_aluno)
    print('Data de Nascimento:', c.dta_nasc)
    n = 1
    for a in c.ta_matricula_collection:
        print('Matricula-{}:'.format(n), a.tb_disciplina.nme_disc)
        n += 1
