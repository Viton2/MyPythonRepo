'''
1-  Crie a superclasse Veiculo com os atributos comuns valor, modelo (corolla, Honda, Pálio etc)
    e km que indica a quilometragem do veículo.
2-  Crie o construtor da classe Veiculo (def __init___ (self, ...) e alguns gets e sets:
3-  Antes do método main, crie a subclasse Carro, que herda da superclasse Veiculo. E o
    construtor com os atributos valor, modelo, km e qtd_portas.
4-  Crie três instâncias da subclasse Carro com quatro, três e dois argumentos, teste
5-  Na classe Carro, sobrescreva o metodo __str__, ele retorna todos os dados (atributos), teste.
6-  Antes do método main, crie a subclasse Moto, que herda a superclasse Veiculo com
    os três atributos comuns e o atributo cilindradas.
7-  Crie duas instâncias da classe Moto com quatro e três argumentos. Teste
8-  Utilize o método vars() para acessar os atributos de Carro e Moto. Ex.: print(vars(objeto))
9-  Use o método __dict__ para acessar os atributos de Carro e Moto. Ex.: print(objeto.__dict__)
10- Crie o método atualiza_valor, ele recebe um valor em reais e não retorna nada. O objetivo
    do método é acrescentar o valor recebido ao valor original de qualquer veículo.
    Faça uma crítica dentro do método e mostre mensagem de erro. Teste.
12- Crie o método atualiza_valor_pct, ele recebe a porcentagem (5, 10, 20 etc) e não retorna
    nada. O método atualiza o valor de qualquer veículo. Faça crítica No método. Teste
13- Crie o método situacao para verificar se o veículo é um veículo zero, veículo seminovo
    ou veículo usado. O veiculo zero tem km igual a zero, seminovo se tiver até 20000 Km e
    veículo usado se tiver mais que 20000 Km. Use o método com os objetos criados.
14- Crie o método situacao_2 para substituir a mensagem 'Veículo zero' por 'Carro zero' ou
    'Moto zero' e assim sucessivamente com as outras mensagens. Teste
'''

class Veiculo(object):
    qtd_veiculo = 0                         # Atributos de classe
    l_veiculo = list()

    @classmethod                            # Metodos de classe
    def get_qtd_veiculo(cls):
        return Veiculo.qtd_veiculo          # return NomeClasse.nomeAtributoClasse

    @classmethod
    def mostra_veiculo(cls):
        print('Veiculos:')
        for objeto in cls.l_veiculo:
            print(objeto)

    @classmethod
    def calcula_ipva(cls):
        for item in cls.l_veiculo:
            print('\n@classmethod - calcula_ipva')
            item.calcula_ipva()

    @classmethod
    def mostra_situacao(cls):
        for item in cls.l_veiculo:
            item.situacao_2()


    def __init__(self, valor, modelo, km=1):
        self.valor = valor
        self.modelo = modelo                # Atributos de instancia
        self.km = km
        Veiculo.qtd_veiculo += 1            # Atualiza os atributos da classe
        Veiculo.l_veiculo.append(self)      # Adiciona o objeto criado na lista l_veiculo

    def get_valor(self):
        return self.valor
    def set_valor(self, nv_valor):
        self.valor = nv_valor

    def get_modelo(self):
        return self.modelo
    def set_modelo(self, nv_mod):
        self.modelo = nv_mod

    def get_km(self):
        return self.km
    def set_km(self, nv_km):
        self.km = nv_km

    def atualiza_valor(self, valor):
        if isinstance(valor, (int, float)):
            if valor > 0:
                self.valor += valor
            else:
                print("ERRO: valor negativo.")
        else:
            print('ERRO: valor nao int ou float.')

    def atualiza_valor_pct(self, pct):
        if isinstance(pct, (int, float)):
            if pct > 0:
                self.valor += self.valor * pct / 100
            else:
                print("ERRO: valor negativo.")
        else:
            print('ERRO: valor nao int ou float.')

    def situacao(self):
        if self.km == 0:
            print('Veiculo Zero.')
        elif self.km <= 20000:
            print('Veiculo Seminovo.')
        else:
            print('Veiculo Usado.')

    def situacao_2(self):
        tpo_veiculo = self.__class__.__name__       # Pega o nome da classe de um objeto
        print(f'- {self.modelo}, R$ {self.valor}')
        if self.km == 0:                            # Gera a mensagem especifica
            print(tpo_veiculo, 'Zero.\n')
        elif self.km <= 20000:
            print(tpo_veiculo, 'Seminovo.\n')
        else:
            print(tpo_veiculo, 'Usado.\n')
