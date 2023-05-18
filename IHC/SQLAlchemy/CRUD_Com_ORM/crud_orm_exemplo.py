import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.sql import func


def incluir():
    print('Informe os dados a seguir para incluir serviço')
    serv = tb_servico()
    serv.dsc_servico = input("Descrição: ")
    serv.vlr_servico = float(input("Valor: "))
    serv.tmp_servico = int(input("Tempo (Horas): "))
    ses.add(serv)
    ses.commit()


def consultar():
    tb_servicos = ses.query(tb_servico).all()
    print('Listagem com todos os serviços')
    for serv in tb_servicos:
        print('-------------------------------------------------------------------')
        print('Descrição:', serv.dsc_servico)
        print('Valor:', serv.vlr_servico, ' / Tempo de execução:', serv.tmp_servico)
    input("\nEnter - Para voltar ao Menu")


def alterar():
    # Descobrindo o menor e maior identificador cadastrado
    menor, maior = ses.query(func.min(tb_servico.idt_servico), func.max(tb_servico.idt_servico)).first()
    print('Alteração de dados de Serviço')
    idt = int(input('Alterar serviço número? [{}-{}]: '.format(menor, maior)))
    serv = ses.query(tb_servico).filter_by(idt_servico=idt).first()
    serv.dsc_servico = input('Descrição [{}]: '.format(serv.dsc_servico))
    serv.vlr_servico = float(input('Valor [{}]: '.format(serv.vlr_servico)))
    serv.tmp_servico = int(input('Tempo em horas [{}]: '.format(serv.tmp_servico)))
    ses.commit()
    input("\nEnter - Para voltar ao Menu")


def excluir():
    # Lista de serviços para apagar
    tb_servicos = ses.query(tb_servico).order_by(tb_servico.vlr_servico.desc()).all()
    for serv in tb_servicos:
        print(serv.idt_servico, serv.dsc_servico, serv.vlr_servico)
    idt = int(input('Qual o número do serviço para excluir? '))
    ses.query(tb_servico).filter(tb_servico.idt_servico == idt).delete()
    ses.commit()
    input("\nEnter - Para voltar ao Menu")


def menu():
    continuar = True
    while continuar:
        print('\n' * 30)
        print('CRUD de Serviços - MENU')
        print('1 - Incluir')
        print('2 - Consultar')
        print('3 - Alterar')
        print('4 - Excluir')
        print('5 - Sair')
        opc = input('Qual a sua opção? ')
        print("\n" * 30)
        if opc == '1':
            incluir()
        elif opc == '2':
            consultar()
        elif opc == '3':
            alterar()
        elif opc == '4':
            excluir()
        elif opc == '5':
            continuar = False
        else:
            print('Opção inválida')
            input()
    # Finalizando o programa

    # Fechando a sessão
    ses.close()
    sys.exit()


# --------------------------------------- VARIÁVEIS GLOBAIS ------------------------------------
# Ligação com o esquema de banco de dados
engine = create_engine("mysql+mysqldb://root:uniceub@localhost/db_work?charset=utf8mb4")

# Mapeamento Objeto Relacional com o SQLAlchemy
DB = automap_base()
DB.prepare(engine, reflect=True)
tb_servico = DB.classes.tb_aluno

# Trabalho com sessões da base agora Objeto-Relacional
session_factory = sessionmaker(bind=engine)
ses = session_factory()
# -------------------------------------------------------------------------------------------------

# Iniciando o programa a partir do menu
menu()
