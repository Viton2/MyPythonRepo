import datetime
from pessoa_2 import Pessoa

if __name__ == '__main__':  # Atalho: mai <tab>
    dta_nascimento_1 = datetime.date(1993, 12, 13)
    pessoa1 = Pessoa("Carlos", 71, 1.80, dta_nascimento_1)  # Chama construtor(__init__)
    # pessoa1 = Pessoa("Carlos", 71, 1.80, datetime.date(1993, 12, 13))     # Equivalente as 2 linhas

    print(pessoa1)  # print(pessoa1.__str__())                  # Chama o metodo __str__
    '''    <pessoa_2.Pessoa object at 0x00000294787168E0>   '''

    nome = pessoa1.get_nome()  # Usando variavel
    print("- Pessoa 1: \nNome:", nome)
    # print("- Pessoa 1: \nNome:", pessoa1.get_nome())            # Equivalente as duas anteriores
    print("dta_nascimento: ", pessoa1.get_dta_nascimento())  # Direto no print
    pessoa1.set_nome("Ailton")
    print('Nome: ', pessoa1.get_nome())

    # nova_data = datetime.date(1985, 12, 13)
    # pessoa1.set_dta_nascimento(nova_data)
    # print("Nova data: ", pessoa1.get_dta_nascimento())
    dta_nascimento_2 = datetime.date(2005, 12, 23)  # Solucao 1
    pessoa1.set_dta_nascimento(dta_nascimento_2)
    # ano = int(input('Ano: '))                                 # Solucao 2
    # mes = int(input('Mes: '))
    # dia = int(input('Dia: '))
    # dta_nascimento_2 = datetime.date(ano, mes, dia)
    # pessoa1.set_dta_nascimento(dta_nascimento_2)
    print("dta_nascimento:", pessoa1.get_dta_nascimento())  # Teste

    print("IMC:", '%.2f' % pessoa1.imc())

    dta_nascimento_3 = datetime.date(2010, 11, 23)
    pessoa2 = Pessoa('Marla', 63, 1.65, dta_nascimento_3)
    print("- Pessoa 2: \nNome:", pessoa2.get_nome())
    print("dta_nascimento: ", pessoa2.get_dta_nascimento())

    pessoa3 = Pessoa('Ana', 61, 1.69)  # Testando valor default para a dta_nascimento
    print("- Pessoa 3: \nNome:", pessoa3.get_nome())
    print("dta_nascimento: ", pessoa3.get_dta_nascimento())

    print(pessoa3.__str__())  # Duas linhas equivalentes, __str__ é opcional
    print(pessoa3)
    print(pessoa1)

    pessoa1.set_dta_nascimento(datetime.date(2000, 12, 13))
    print("Idade 1: ", pessoa1.calcula_idade())
    print("Idade 2: ", pessoa2.calcula_idade())
    print("Idade 3: ", pessoa3.calcula_idade())

    pessoa1.mais_velho(pessoa2)
    pessoa1.mais_velho(pessoa3)
