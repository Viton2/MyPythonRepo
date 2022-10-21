'''

- Exercícios:
1. Crie uma classe com o método construtor e pelo menos dois atributos.
2. Crie os métodos gets e sets dos atributos
3. Crie pelo menos um método funcional
4. Teste (use) a classe criada no método main, crie pelo menos dois objetos dessa classe e use todos os métodos desenvolvidos na classe.


'''

class Produto(object):
    def __init__(self, nome, marca, valor=0.00):
        self.nome = nome
        self.valor = valor
        self.marca = marca

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_valor(self):
        return self.valor
    def set_valor(self, novo_valor):
        if novo_valor > 0:
            self.valor = novo_valor
        else:
            print('Erro: Digite um valor válido.')

    def get_marca(self):
        return self.marca
    def set_marca(self, nova_marca):
        self.marca = nova_marca

    def mostra_dados(self):
        print('Nome do produto: ', self.nome)
        print('Valor do produto: ', '%.2f' % self.valor)
        print('Marca do produto: ', self.marca)


if __name__ == '__main__':
    produto1 = Produto('Ketchup', 'Heinz', 10.99)

    produto1.set_valor(-10.99)  # Teste da mensagem de erro

    novo_nome = input('Novo produto: ')
    produto1.set_nome(novo_nome)

    continuar = True
    while continuar:
        novo_valor = float(input('Novo valor: '))
        produto1.set_valor(novo_valor)
        if novo_valor > 0:
            produto1.set_valor(novo_valor)
            continuar = False
            break

    nova_marca = input('Nova marca: ')
    produto1.set_marca(nova_marca)

    print('======================================')         #Mostrando dados apenas com o print (usando os gets)
    print('Produto: ', produto1.get_nome())
    print('Valor: R$', '%.2f' % produto1.get_valor())
    print('Marca: ', produto1.get_marca())

    print('======================================')
    produto1.mostra_dados()                                 #Mostrando dados com o método definido
    print('======================================')

    produto2 = Produto('Maionese', 'Hellmans', 9.99)

    novo_nome = input('Novo produto: ')
    produto2.set_nome(novo_nome)

    continuar = True                                        #Estrutura de repetição para que seja inserido um valor positivo
    while continuar:
        novo_valor = float(input('Novo valor: '))
        produto2.set_valor(novo_valor)
        if novo_valor > 0:
            produto2.set_valor(novo_valor)
            continuar = False
            break

    nova_marca = input('Nova marca: ')
    produto2.set_marca(nova_marca)

    print('======================================')         #Mostrando dados apenas com o print (usando os gets)
    print('Produto: ', produto2.get_nome())
    print('Valor: R$', '%.2f' % produto2.get_valor())
    print('Marca: ', produto2.get_marca())

    print('======================================')
    produto2.mostra_dados()                                 #Mostrando dados com o método definido
    print('======================================')