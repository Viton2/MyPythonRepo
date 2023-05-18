from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from prettytable import PrettyTable

# --------------------------------------- VARIÁVEIS GLOBAIS ------------------------------------
# Ligação com o esquema de banco de dados
engine = create_engine("mysql+mysqldb://root:uniceub@localhost/db_work?charset=utf8mb4")

# Mapeamento Objeto Relacional com o SQLAlchemy
DB = automap_base()
DB.prepare(engine, reflect=True)
tb_servico = DB.classes.tb_aluno
tb_cliente = DB.classes.tb_disciplina
ta_agendamento = DB.classes.ta_matricula

# Trabalho com sessões da base agora Objeto-Relacional
session_factory = sessionmaker(bind=engine)
ses = session_factory()
# -------------------------------------------------------------------------------------------------

continuar = True
while continuar:
    print("\n" * 30)

    clientes = ses.query(tb_cliente).all()
    tab = PrettyTable(["Identificador", "Cliente", "Telefone"])
    for c in clientes:
        tab.add_row([c.idt_cliente, c.nme_cliente, c.tel_cliente])
    print(tab)
    idt = int(input('Agendar serviço para o cliente Nº? '))
    cli = ses.query(tb_cliente).filter_by(idt_cliente=idt).first()

    if cli == None:
        input("Cliente não encontrado. Tecle [Enter] Para recomeçar.")
        continue

    print("\n" * 30)
    # Listar os serviços disponíveis
    servicos = ses.query(tb_servico).all()
    print('Catálogo de Serviços')
    tabServ = PrettyTable(["Identificador", "Descrição", "Valor", "Tempo"])
    for s in servicos:
        tabServ.add_row([s.idt_servico, s.dsc_servico, ("R$" + str(s.vlr_servico)),
                         (str(s.tmp_servico) + ' hora(s)')])
    print(tabServ)

    print('Cliente:', cli.nme_cliente)
    idt = int(input('Qual número do serviço para agendar? '))
    dta = input('Qual a data do agendamento [DD/MM/AAAA]? ')
    hor = input('Qual a hora do agendamento [HH:MM]? ')

    serv = ses.query(tb_servico).filter_by(idt_servico=idt).first()

    if serv == None:
        input("Serviço não encontrado. Clique [Enter] para recomeçar.")
        continue

    # Incluindo um novo agendamento
    a = ta_agendamento()
    a.tb_disciplina = cli
    a.tb_aluno = serv
    a.dti_agendamento = dta[6:10] + "-" + dta[3:5] + "-" + dta[0:2] + ' ' + hor
    ses.add(a)
    ses.commit()

    # Listar os agendamentos do cliente
    print("\n" * 30)
    print('Cliente:', cli.nme_cliente)
    tabAgend = PrettyTable(["Descrição do Serviço", "Valor", "Agendamento"])
    for a in cli.ta_agendamento_collection:
        tabAgend.add_row([a.tb_aluno.dsc_servico, a.tb_aluno.vlr_servico,
                          a.dti_agendamento])
    print(tabAgend)
    opc = input('Fazer mais um agendamento [S-N]? ')
    if opc.upper() == 'N':
        continuar = False

ses.close()
