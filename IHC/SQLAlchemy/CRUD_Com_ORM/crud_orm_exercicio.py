import datetime
import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func


def incluir():
    print('Informe os dados a seguir para incluir serviço')
    aluno = tb_aluno()
    aluno.nme_aluno = input("Nome: ")
    data = input("Data de nascimento no formato DD/MM/AAAA: ")
    dia, mes, ano = map(int, data.split('/'))
    data = datetime.date(ano, mes, dia)
    aluno.dta_nasc = data
    ses.add(aluno)
    ses.commit()


def consultar():
    aluno = ses.query(tb_aluno).all()
    print('Listagem com todos os serviços')
    for a in aluno:
        print('-------------------------------------------------------------------')
        print('Id:', a.idt_aluno)
        print('Nome:', a.nme_aluno)
        print('Valor:', a.dta_nasc)
    input("\nEnter - Para voltar ao Menu")


def alterar():
    menor, maior = ses.query(func.min(tb_aluno.idt_aluno), func.max(tb_aluno.idt_aluno)).first()
    print('Alteração de dados de Aluno')
    idt = int(input('Alterar serviço número? [{}-{}]: '.format(menor, maior)))
    aluno = ses.query(tb_aluno).filter_by(idt_aluno=idt).first()
    aluno.nme_aluno = input('Nome [{}]: '.format(aluno.nme_aluno))
    data = input("Data de nascimento no formato DD/MM/AAAA [{}]: ".format(aluno.dta_nasc))
    dia, mes, ano = map(int, data.split('/'))
    data = datetime.date(ano, mes, dia)
    aluno.dta_nasc = data
    ses.commit()
    input("\nEnter - Para voltar ao Menu")


def excluir():
    aluno = ses.query(tb_aluno).order_by(tb_aluno.idt_aluno.desc()).all()
    for a in aluno:
        print(a.idt_aluno, a.nme_aluno, a.dta_nasc)
    idt = int(input('Qual o ID do aluno para excluir? '))
    ses.query(tb_aluno).filter(tb_aluno.idt_aluno == idt).delete()
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

    ses.close()
    sys.exit()


# --------------------------------------- VARIÁVEIS GLOBAIS ------------------------------------
engine = create_engine("mysql+mysqldb://root:uniceub@localhost/db_studies?charset=utf8mb4")

DB = automap_base()
DB.prepare(engine, reflect=True)
tb_aluno = DB.classes.tb_aluno

session_factory = sessionmaker(bind=engine)
ses = session_factory()
# -------------------------------------------------------------------------------------------------

menu()
