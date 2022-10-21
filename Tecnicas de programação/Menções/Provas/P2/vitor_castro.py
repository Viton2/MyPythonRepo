'''
Vitor Castro de Oliveira

1. Crie a classe conta corrente com as características nome do titular, número da conta , saldo.
Crie o método construtor recebendo self e os três parâmetros, coloque pelo menos um desses parâmetros com valor default (padrão).
Crie pelo menos um método get e pelo menos um método set e faça crítica no método set.
Crie o método funcional depósito, ele recebe um valor que será depositado na conta corrente, faça crítica.

No método main, instancie dois objetos dessa classe.
Crie o objeto conta1 passando os três argumentos e o crie o objeto conta2 passando apenas dois argumentos.
Use (teste) todos os método criados na classe para os objetos conta1 e conta2.

Elabore o enunciado e a implementação de mais um método funcional na classe criada.
 A complexidade do enunciado e da implementação do método serão considerados para mensurar a avaliação do método.
Obs.: este método deve ser diferente dos métodos vistos nos exemplos usados nas aulas.

ENUNCIADO: Crie o metodo 'emprestimo' que mostra se o titular da conta tem direito a pegar um emprestimo e, se puder, mostre tambem
o valor maximo que o titular tem direito. Se o saldo for menor que 3500, o titular nao pode, se o saldo for entre 3500 e 10000 pode pegar emprestimo de ate 8000,
se for entre 10000 e 35000 pode pegar de ate 25000, e se o saldo for acima de 35000 pode pegar de ate 100000.

- Vale 50%

2. Implemente um projeto usando o conceito de POO com herança contendo a superclasse (classe pai) Veiculo e duas subclasses (classes filhas) Carro e Ônibus.
A superclasse Veículo tem os atributos de instância placa e preço, o construtor (__init__) e os métodos get e set referente aos atributos.
O construtor da superclasse recebe os parâmetros e armazena nos respectivos atributos de instância.
A subclasse Carro tem os atributos de instância placa, preço e quantidade de portas, o construtor,
o método set referente ao atributo quantidade de porta, faça pelo menos uma crítica nesse método.
E o método calcula ipva, ele não recebe nada e faz o cálculo do ipva aplicando 3% sobre o valor do carro.
O construtor da subclasse Carro recebe os três parâmetros e chama o construtor da superclasse enviado os atributos que são tratados na superclasse Veículo.
E a subclasse Ônibus tem os atributos de instância placa, preço e capacidade, ou seja,
a quantidade de passageiros, o construtor e o método set referente ao atributo capacidade, faça uma crítica nesse método set.
O construtor da subclasse Ônibus recebe três parâmetros e chama o construtor da superclasse enviando os atributos que são tratados na superclasse Veículo.
Crie o método que retorna todos os dados do ônibus formatados.
O sistema precisa saber quantos veículos tem cadastrada. Crie o atributo de classe e o método de classe necessário para atender essa necessidade.
No método main, crie um objeto de cada subclasse. E teste os métodos do sistema com os objetos instanciados.
- Vale 50%
'''

class Conta_Corrente(object):
    def __init__(self, nome, numero_conta, saldo=0.0):
        self.nome = nome
        self.numero = numero_conta
        self.saldo = saldo

    def get_saldo(self):
        return self.saldo
    def set_saldo(self, nv_saldo):
        if isinstance(nv_saldo, (int, float)):
            if nv_saldo > 0:
                self.saldo = nv_saldo
            else:
                print('ERRO: Valor negativo.')
        else:
            print('ERRO: Valor nao int ou float.')

    def deposito(self, dpst):
        if isinstance(dpst, (int, float)):
            if dpst > 0:
                self.saldo += dpst
            else:
                print('ERRO: Valor negativo.')
        else:
            print('ERRO: Valor nao int ou float.')

    def emprestimo(self):       # Questao de criar um enunciado (Enunciado embaixo da questao)
        if self.saldo < 3500:
            print('Voce nao pode pedir emprestimo.\n')
        elif self.saldo >= 3500 and self.saldo < 10000:
            print('Voce pode pedir emprestimo de ate R$ 8000,00.\n')
        elif self.saldo >= 10000 and self.saldo < 35000:
            print('Voce pode pedir emprestimo de ate R$ 25000,00.\n')
        else:
            print('Voce pode pedir emprestimo de ate R$ 100000,00.\n')

class Veiculo(object):
    qnt_veiculos = 0

    @classmethod
    def get_qnt_veiculos(cls):
        return Veiculo.qnt_veiculos

    def __init__(self, placa, preco):
        self.placa = placa
        self.preco = preco
        Veiculo.qnt_veiculos += 1

    def get_placa(self):
        return self.placa
    def set_placa(self, nv_placa):
        self.placa = nv_placa

    def get_preco(self):
        return self.preco
    def set_preco(self, nv_preco):
        self.preco = nv_preco

class Carro(Veiculo):
    def __init__(self, placa, preco, qnt_porta):
        super().__init__(placa, preco)
        self.qnt_porta = qnt_porta

    def set_qnt_porta(self, nv_qnt):
        if isinstance(nv_qnt, int):
            if nv_qnt > 0:
                self.qnt_porta = nv_qnt
            else:
                print('ERRO: Valor negativo.\n')
        else:
            print('ERRO: Valor nao int.\n')

    def calcula_ipva(self):
        ipva = self.preco * 0.03
        print(f'IPVA desse Carro: {ipva}\n')

class Onibus(Veiculo):
    def __init__(self, placa, preco, capacidade):
        super().__init__(placa, preco)
        self.capacidade = capacidade

    def set_capacidade(self, nv_cp):
        if isinstance(nv_cp, int):
            self.capacidade = nv_cp
        else:
            print('Digite um valor inteiro maior que 0.\n')

    def retorna_dados(self):
        s = print(f'Placa: {self.placa}, Preco: {self.preco}, Capacidade: {self.capacidade}')
        return s


if __name__ == '__main__':
    conta1 = Conta_Corrente('Vitor', 23232, 15000)
    conta2 = Conta_Corrente('Julia', 45643)

    conta1.set_saldo(20000)
    conta1.deposito(1000)
    print(f'Saldo da conta 1: {conta1.get_saldo()}')
    conta1.emprestimo()

    conta2.set_saldo(50000)
    conta2.deposito(500)
    print(f'Saldo da conta 2: {conta2.get_saldo()}')
    conta2.emprestimo()

    carro1 = Carro('ABC-4000', 40000, 4)
    onibus1 = Onibus('DEF-2001', 180000, 80)

    print(f'Quantidade de Veiculos: {Veiculo.get_qnt_veiculos()}\n')

    carro1.set_placa('OAB-2020')
    print(f'Placa do carro: {carro1.get_placa()}')
    carro1.set_preco(70000)
    print(f'Preco do carro: {carro1.get_preco()}')
    carro1.set_qnt_porta(2)
    carro1.calcula_ipva()

    onibus1.set_placa('MLG-1929')
    print(f'Placa do onibus: {onibus1.get_placa()}')
    onibus1.set_preco(250000)
    print(f'Preco do Onibus: {onibus1.get_preco()}')
    onibus1.set_capacidade(100)
    onibus1.retorna_dados()
