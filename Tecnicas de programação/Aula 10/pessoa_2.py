import datetime


class Pessoa(object):
    def __init__(self, nome, peso, altura, dta_nascimento=datetime.date(2000, 1, 21)):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.dta_nascimento = dta_nascimento

    def get_nome(self):
        return self.nome

    # def set_nome(self, novo_nome):         # Sem crítica
    # self.nome = novo_nome
    def set_nome(self, novo_nome):  # Com crítica
        # if type(novo_nome) == str:        # Duas linhas equivalentes
        if isinstance(novo_nome, str):
            if len(novo_nome) >= 2:
                self.nome = novo_nome
            else:
                print('ERRO: Nome Inválido')
        else:
            print('ERRO: Tipo Inválido')

    def get_dta_nascimento(self):
        return self.dta_nascimento

    def set_dta_nascimento(self, nova_data):
        self.dta_nascimento = nova_data

    def imc(self):  # Metodos funcionais
        #   vl_imc = self.peso / (self.altura ** 2)             #1
        vl_imc = self.peso / pow(self.altura, 2)  # 2
        return vl_imc
        # return self.peso / (self.altura * self.altura)        #3      # Equivalente as 2 de cima

    def __str__(self):  # Sobrescrevendo o metedo especial __str__
        # s = self.get_nome() + ' ' + str(self.peso) + ', ' + str(self.get_dta_nascimento())
        # s = "{} {}, {}" .format(self.nome, self.peso, self.dta_nascimento)    # .format
        # s = f"{self.get_nome()}, {self.peso} {self.get_dta_nascimento()}      # Usa metodos gets
        s = f'{self.nome}, {self.peso}, {self.dta_nascimento}'  # f-string
        return s
        # return f"Nome: {self.nome}, Peso: {self.peso}, Nascimento: {self.dta_nascimento}"

    def calcula_idade(self):
        hoje = datetime.date.today()  # Data completa de hoje (ano, mes, dia)
        idade = hoje.year - self.dta_nascimento.year  # year pega o ano de uma data
        # return idade
        # Dica: Teste os meses de hoje e da data de aniversario
        if hoje.month < self.dta_nascimento.month:
            idade -= 1
        # Dica: Se os meses forem iguais, precisa testar os dias tambem
        elif hoje.month == self.dta_nascimento.month and hoje.day < self.dta_nascimento.day:
            idade -= 1
        return idade

    def mais_velho(self, outra_pessoa):
        if self.calcula_idade() > outra_pessoa.calcula_idade():
            print("Data de nascimento do mais velho: ", self.dta_nascimento)
            print("Data de nascimento do mais novo: ", outra_pessoa.dta_nascimento)
        elif self.calcula_idade() < outra_pessoa.calcula_idade():
            print("Data de nascimento do mais velho: ", outra_pessoa.dta_nascimento)
            print("Data de nascimento do mais novo: ", self.dta_nascimento)
        else:
            print("Tem a mesma idade!")
