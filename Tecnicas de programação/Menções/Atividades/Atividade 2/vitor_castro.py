'''

- Exercícios:

1. Crie uma classe com o método construtor e pelo menos três atributos. E use dois atributos com valor default (padrão).

2. Crie os métodos gets e sets dos atributos.

3. Crie pelo menos dois métodos funcional.

4. No método main, teste (use) a classe criada, crie pelo menos três objetos dessa classe, um objeto passando três argumentos, um objeto
 passando dois argumentos e um objeto passando um argumento.

5. E teste (use) todos os métodos desenvolvidos na classe.

Obs.: crie a classe e os métodos funcionais diferentes dos desenvolvidos durante as aulas.


'''

class Jogo(object):
    def __init__(self, titulo, preco=0.00, faixa_etaria=''):
        self.titulo = titulo
        self.preco = preco
        self.faixa_etaria = faixa_etaria

    def get_titulo(self):
        return self.titulo
    def set_titulo(self, nv_titulo):
        self.titulo = nv_titulo

    def get_preco(self):
        return self.preco
    def set_preco(self, nv_preco):
        self.preco = nv_preco

    def get_faixa_etaria(self):
        return self.faixa_etaria
    def set_faixa_etaria(self, nv_faixa_etaria):
        self.faixa_etaria = nv_faixa_etaria

    def checar_faixa_etaria(self):
        if self.faixa_etaria == '18':
            print("Esse jogo nao eh recomendado para menores de 18 anos!")
        elif self.faixa_etaria == '16':
            print("Esse jogo nao eh recomendado para menores de 16 anos!")
        elif self.faixa_etaria == '14':
            print("Esse jogo nao eh recomendado para menores de 14 anos!")
        elif self.faixa_etaria == '12':
            print("Esse jogo nao eh recomendado para menores de 12 anos!")
        elif self.faixa_etaria == '10':
            print("Esse jogo nao eh recomendado para menores de 10 anos!")
        elif self.faixa_etaria == 'L' or self.faixa_etaria == 'l':
            print("Esse jogo tem classificacao indicativa Livre!")
        else:
            print("Valor invalido.")

    def verificar_compra(self, valor):
        if isinstance(valor, float):
            if valor >= float(self.preco):
                print("Valor suficiente para comprar esse jogo!\nO seu troco sera de: R$", float(valor - float(self.preco)))
            else:
                print("Valor insuficiente.")
        else:
            print("Digite um valor válido.")

if __name__ == '__main__':
    jogo1 = Jogo('GTA V', 150.00, '18')
    jogo2 = Jogo('Forza Horizon', 220.00)
    jogo3 = Jogo('COD')

    print('Titulo do jogo 1: ', jogo1.get_titulo())         # Testes jogo1
    novo_titulo = input('Digite um novo titulo: ')
    jogo1.set_titulo(novo_titulo)
    print('Novo titulo do jogo 1: ', jogo1.get_titulo())

    print('Preco do jogo 1: R$', jogo1.get_preco())
    novo_preco = float(input('Digite um novo preco: R$'))
    jogo1.set_preco(novo_preco)
    print('Novo preco do jogo 1: R$', jogo1.get_preco())

    print('Faixa etaria do jogo 1: ', jogo1.get_faixa_etaria())
    novo_faixa_etaria = input('Digite uma nova faixa etaria: ')
    jogo1.set_faixa_etaria(novo_faixa_etaria)
    print('Nova faixa etaria do jogo 1: ', jogo1.get_faixa_etaria())

    jogo1.checar_faixa_etaria()

    jogo1.verificar_compra(float(input("Digite o valor em dinheiro para a compra: ")))

    print('Titulo do jogo 2: ', jogo2.get_titulo())     # Testes jogo2
    novo_titulo = input('Digite um novo titulo: ')
    jogo2.set_titulo(novo_titulo)
    print('Novo titulo do jogo 2: ', jogo2.get_titulo())

    print('Preco do jogo 2: R$', jogo2.get_preco())
    novo_preco = input('Digite um novo preco: R$')
    jogo2.set_preco(novo_preco)
    print('Novo preco do jogo 2: R$', jogo2.get_preco())

    print('Faixa etaria do jogo 2: ', jogo2.get_faixa_etaria())
    novo_faixa_etaria = input('Digite uma nova faixa etaria: ')
    jogo2.set_faixa_etaria(novo_faixa_etaria)
    print('Nova faixa etaria do jogo 2: ', jogo2.get_faixa_etaria())

    jogo2.checar_faixa_etaria()

    jogo2.verificar_compra(float(input("Digite o valor em dinheiro para a compra: ")))

    print('Titulo do jogo 3: ', jogo3.get_titulo())     # Testes jogo3
    novo_titulo = input('Digite um novo titulo: ')
    jogo3.set_titulo(novo_titulo)
    print('Novo titulo do jogo 3: ', jogo3.get_titulo())

    print('Preco do jogo 3: R$', jogo3.get_preco())
    novo_preco = input('Digite um novo preco: R$')
    jogo3.set_preco(novo_preco)
    print('Novo preco do jogo 3: R$', jogo3.get_preco())

    print('Faixa etaria do jogo 3: ', jogo3.get_faixa_etaria())
    novo_faixa_etaria = input('Digite uma nova faixa etaria: ')
    jogo3.set_faixa_etaria(novo_faixa_etaria)
    print('Nova faixa etaria do jogo 3: ', jogo3.get_faixa_etaria())

    jogo3.checar_faixa_etaria()

    jogo3.verificar_compra(float(input("Digite o valor em dinheiro para a compra: ")))