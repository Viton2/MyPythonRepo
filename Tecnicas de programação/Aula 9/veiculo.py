'''


1- Crie a classe Veiculo
2- Crie o construtor da classe com os atributos: modelo, ano, valor
3- No main, crie pelo menos dois objetos da classe. Teste
4- Crie os métodos gets e sets do atributo modelo. Teste
5- Altere o modelo do veiculo. Teste
6- Altere o valor do veiculo, crie o método set_valor. Teste
7- Faça uma crítica no método set_valor para evitar dados inconsistentes. Teste
8- Crie o método mostra_dados. Ele mostra todos os atributos da classe. Teste
9- Crie o metodo retorna_dados, ele retorna os dados (atributos) concatenados. Teste
10- Crie o metodo aumento_valor. Ele recebe o valor do aumento que será acrescentado ao atributo valor do carro. Teste
11- Peça pro usuário fornecer o valor do aumento do veículo. Teste
12- Altere o contrutor para o usuário instanciar um objeto sem valor, valor default 0.
   Ele fornece somente o modelo e ano. Teste, crie um novo objeto (veiculo) só com o modelo e ano.
13- Crie mais um objeto passando apenas o modelo do veiculo, teste
14- Crie o método compara_valor, ele compara o valor de dois carros quaisquer e mostra o valor
    do carro mais caro ou a mensagem "Tem o mesmo valor.". Teste


'''


class Veiculo(object):  # Nome de classe começa com letra maiuscula e as outras letras minusculas
    # def __init__(self, modelo, ano, valor):             #Atalho: def _ <tab>    # Construtor
    # def __init__(self, modelo, ano, valor=0.00):        #Construtor com um valor default
    def __init__(self, modelo, ano=2021, valor=0.00):  # Construtor com dois valores default
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def get_modelo(self):  # Metodos gets e sets
        return self.modelo

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def get_valor(self):
        return self.valor

    # def set_valor(self, novo_valor):            #Sem crítica
    #       self.valor = novo_valor
    def set_valor(self, novo_valor):  # Com critica
        if novo_valor > 0:
            self.valor = novo_valor
        else:
            print('Erro: valor inconsistente, valor negativo.')

    def mostra_dados(self):  # Metodos funcionais
        print('Modelo:', self.modelo)
        print('Ano', self.ano)
        print('Valor', self.valor)

    def retorna_dados(self):
        # dados = self.modelo + ', ' + str(self.ano) + ', ' + str(self.valor)   #Concatenação
        # dados = self.get_modelo() + ', ' + str(self.ano) + ', ' + str(self.get_valor())
        # dados = '%s, %d, %.2f' % (self.modelo, self.ano, self.valor)
        # dados = '{}, {}, {}' .format(self.modelo, self.ano, self.valor)
        dados = f'{self.modelo}, {self.ano}, {self.valor}'  # f-string
        return dados

    def aumento_valor(self, valor_aumento):
        self.valor += valor_aumento  # self.valor = self.valor + valor_aumento

    # No main, carro1.compara_valor(carro2)                 #carro1 - (self) e carro2 - (outro_objeto)
    def compara_valor(self, outro_objeto):  # Recebe dois objetos
        if self.valor > outro_objeto.valor:
            print('Carro mais caro: R$', self.valor)  # Valor do objeto carro1
            print('Carro mais barato: R$', outro_objeto.valor)
        elif self.valor < outro_objeto.valor:
            print('Carro mais caro: R$', outro_objeto.valor)  # Valor do objeto carro2
            print('Carro mais barato: R$', self.valor)
        else:
            print('Tem o mesmo valor.')
