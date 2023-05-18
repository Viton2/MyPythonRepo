from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from datetime import timedelta

# ----- VARIÁVEIS GLOBAIS ------------------------------------
# Ligação com o esquema de banco de dados
engine = create_engine("mysql+mysqldb://root:uniceub@localhost/db_work?charset=utf8mb4")

# Mapeamento Objeto Relacional com o SQLAlchemy
DB = automap_base()
DB.prepare(engine, reflect=True)
tb_servico = DB.classes.tb_servico
tb_cliente = DB.classes.tb_cliente
ta_agendamento = DB.classes.ta_agendamento

# Trabalho com sessões da base agora Objeto-Relacional
session_factory = sessionmaker(bind=engine)
ses = session_factory()
#------------------------------------------------------------

agendamentos = ses.query(ta_agendamento).all()

for a in agendamentos:
   print(a.tb_cliente.nme_cliente, a.tb_servico.dsc_servico, a.tb_servico.vlr_servico, a.dti_agendamento)

clientes = ses.query(tb_cliente).all()

for c in clientes:
    print('-' * 50)
    print('Nome:', c.nme_cliente)
    print('Endereço:', c.end_cliente)
    print('Telefone:', c.tel_cliente)
    n = 1
    for a in c.ta_agendamento_collection:
        print('Agendamento-{}:'.format(n), 'de', a.dti_agendamento, 'às',
            a.dti_agendamento + timedelta(hours=a.tb_servico.tmp_servico), a.tb_servico.dsc_servico,
            '(R$ {})'.format(a.tb_servico.vlr_servico))
        n += 1
