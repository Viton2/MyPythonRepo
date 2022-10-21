'''
1- Crie a classe Produto.
2- O construtor da classe com os atributos: nome, vlr_compra, vlr_venda, qtd_estoque, qtd_minima
3- No main, crie o primeiro objeto da classe com estes dados: Arroz, 15.00, 19.50, 67, 20. Teste
4- Crie os métodos gets e sets dos atributos: nome, qtd_estoque e qtd_minima. Teste.
5- Altere a quantidade minima para um valor digitado. Teste.
6- Faça uma crítica nos métodos set_nome e set qtd_estoque. Teste
7- Crie o método set_vlr_compra com crítica. Teste
8- Sobrescreva o método __str__ . Ele não recebe nada e retorna todos os atributos. Teste.
9- Crie o método lucro. Não recebe nada e retorna o valor do lucro do produto. Teste
10- Método atualiza_estoque. Ele recebe a quantidade vendida de produtos e atualiza.
    E não retorna nada, Teste
11- Crie o método alerta_estoque. Não recebe nada e retorna um valor booleano. Retorna True,
   se a quantidade em estoque for menor que a quantidade mínima. Senão, retorna False. Teste

13- Crie o segundo objeto da classe passando como argumento apenas o nome do produto, teste
14- No main, crie mais um objeto da classe passando como argumento apenas o nome e a quantidade
    em estoque. Teste
15- No main, crie mais um objeto da classe passando como argumento apenas o nome e o valor de
    compra. Teste
'''

class Produto(object):
    def __init__(self, nome, vlr_compra=0.0, vlr_venda=0.0, qtd_estoque=0, qtd_minima=0):
        self.nome = nome
        self.vlr_compra = vlr_compra
        self.vlr_venda = vlr_venda
        self.qtd_estoque = qtd_estoque
        self.qtd_minima = qtd_minima

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.nome = novo_nome
        else:
            print("ERRO: Digite um nome válido!")

    def get_qtd_estoque(self):
        return self.qtd_estoque
    def set_qtd_estoque(self, novo_qtd_estoque):
        if isinstance(novo_qtd_estoque, int):
            self.qtd_estoque = novo_qtd_estoque
        else:
            print("ERRO: Digite um valor válido!")

    def get_qtd_minima(self):
        return self.qtd_minima
    def set_qtd_minima(self, novo_qtd_minima):
        self.qtd_minima = novo_qtd_minima

    def set_vlr_compra(self, novo_vlr_compra):
        if isinstance(novo_vlr_compra, float):
            self.vlr_compra = novo_vlr_compra
        else:
            print("ERRO: Digite um valor válido!")

    def __str__(self):
        s = f'Nome: {self.nome}, Valor de compra: {self.vlr_compra}, Valor de venda: {self.vlr_venda}, '\
        f'Quantidade de estoque: {self.qtd_estoque}, Quantidade Minima: {self.qtd_minima}'
        return s

    def lucro(self):
        vlr_lucro = self.vlr_venda - self.vlr_compra
        return vlr_lucro

    def atualiza_estoque(self, qtd_vendida):
        self.qtd_estoque -= qtd_vendida

    def alerta_estoque(self):       # Retorna um valor Booleano
        if self.qtd_estoque < self.qtd_minima:
            ret = True
        else:
            ret = False
        return ret

    def repor_produto(self, qtd_comprada):
        self.qtd_estoque += qtd_comprada

    def maior_qtd(self, objeto2):
        if self.qtd_estoque > objeto2.qtd_estoque:
            print("Maior quantidade: ", self.get_nome())
        elif objeto2.qtd_estoque > self.qtd_estoque:
            print("Maior quantidade: ", objeto2.get_nome())
        else:
            print("Valores iguais!")

if __name__ == '__main__':
    produto1 = Produto('Arroz', 15.00, 19.50, 67, 20)
    print(produto1)                 #Duas linhas equivalentes (90 e 91)
    print(produto1.__str__())

    produto1.set_qtd_minima(33)
    print("Qtd. Minima: ", produto1.get_qtd_minima())
    produto1.set_qtd_estoque(50)
    produto1.set_vlr_compra(23.90)
    print("Lucro: ", produto1.lucro())
    produto1.atualiza_estoque(10)
    print("Novo estoque: ", produto1.get_qtd_estoque())

    if produto1.alerta_estoque():
        print("Presisa comprar!")
    else:
        print("Nao precisa comprar!")

    produto1.repor_produto(40)
    print("Novo estoque: ", produto1.get_qtd_estoque())

    produto2 = Produto('Batata')
    print(produto2)

    produto3 = Produto('Feijao', qtd_estoque=50)
    print(produto3)

    produto4 = Produto('Cebola', 10)
    print(produto4)

    produto1.maior_qtd(produto2)
    produto3.maior_qtd(produto1)