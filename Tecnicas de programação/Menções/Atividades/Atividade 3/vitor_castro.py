import datetime
'''

- Exercícios:

1. Crie uma superclasse com o método construtor e pelo menos um atributo. OK

2. Crie os métodos gets e sets do atributo da superclasse. OK

3. Crie pelo menos um método funcional na superclasse. OK

4. Crie uma subclasse com o método construtor e pelo menos dois atributos. OK

5. Crie os métodos gets e sets dos atributos da superclasse. OK

6. No método main, teste (use) as classes criadas, crie pelo menos um objeto da superclasse e pelo menos um objeto da subclasse. OK

7. E teste (use) todos os métodos desenvolvidos nas classes. OK

'''

class Animal(object):
    def __init__(self, nome, idade=''):
        self.nome = nome
        self.idade = idade

    def get_nome(self):
        return self.nome
    def set_nome(self, nv_nome):
        self.nome = nv_nome

    def get_idade(self):
        return self.idade
    def set_idade(self, nv_idade):
        self.idade = nv_idade

    def definir_idade(self):
        data_atual = datetime.datetime.now()
        data = data_atual.date()
        ano = int(data.strftime('%Y'))
        nasc = int(input(f'Digite o ano de nascimento do animal: '))
        self.idade = ano - nasc
        print(f'Idade do seu animal: {self.idade} ano(s)/mes(es)')

class Cachorro(Animal):
    def __init__(self, nome, idade, raca, altura=0.0):
        super().__init__(nome, idade)
        self.raca = raca
        self.altura = altura

    def get_raca(self):
        return self.raca
    def set_raca(self, nv_raca):
        self.raca = nv_raca

    def get_altura(self):
        return self.altura
    def set_altura(self, nv_altura):
        self.altura = nv_altura


if __name__ == '__main__':
    a1 = Animal('Minho', '10 meses')
    print('Nome: ', a1.get_nome())
    a1.set_nome('Rex')
    print('Novo nome: ', a1.get_nome())
    print('Idade: ', a1.get_idade())
    a1.set_idade('2 anos')
    print('Nova idade: ', a1.get_idade())
    a1.definir_idade()

    c1 = Cachorro('Cookie', '2 anos', 'Pitbull', 0.50)
    print(f'Nome: {c1.get_nome()}, Idade: {c1.get_idade()}, Raça: {c1.get_raca()}, Altura: {c1.get_altura()}')
    c1.set_nome('Toby')
    c1.set_idade('3 anos')
    c1.set_raca('Pincher')
    c1.set_altura(0.3)
    print(f'Nome: {c1.get_nome()}, Idade: {c1.get_idade()}, Raça: {c1.get_raca()}, Altura: {c1.get_altura()}')
    c1.definir_idade()