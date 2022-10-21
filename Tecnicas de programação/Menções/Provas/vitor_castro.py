'''
IMPORTANTE: Orientações para o envio da resolução da avaliação:
- Hoje não tem chamada e a avaliação é individual.
- Permaneçam na sala Google Meet durante a realização da avaliação.
- Envie a resolução da avaliação antes das 21h20.
- Envie as questões num único arquivo .py
- Coloque o primeironome, o underline e o segundonome no nome do arquivo “.py”
   Layout: primeironome_segundonome.py
   Exemplo: ailton_pinheiro.py

ALUNO: VITOR CASTRO DE OLIVEIRA

1. Resolva estes itens com funções de lista:

a. Crie uma lista vazia e acrescente alguns valores numéricos usando pelo menos dois métodos diferentes.
b. Calcule o mostre a média dos valores na lista.
c. Calcule o mostre a porcentagem dos valores negativos na lista.
d. Elabore mais um enunciado e a implementação de mais uma questão na lista criada.
Não faça exercício igual aos ministrados nas aulas.

      D)  ---[Remova algum elemento da lista]---

A complexidade do enunciado e da implementação da questão serão considerados para mensurar a avaliação da questão.
- Vale 40%


2. Crie a classe Livro com os atributos título, autor, páginas e preço. Crie o método construtor que além do parâmetro self
recebe mais quatro parâmetros que serão atribuídos aos respectivos atributos da classe Livro.
Coloque pelo menos um desses atributos com valor default (padrão)
Crie pelo menos um método get e pelo menos um método set e faça crítica no método set.

Crie o método funcional aumento_preco com o objetivo de atualizar o preço do livro.
Esse método recebe o valor do aumento e atualiza o atributo preco.

No método main, instancie dois objetos dessa classe.
Crie o objeto livro1 passando os quatro argumentos e o crie o objeto livro2 passando apenas três argumentos.
Use (teste) todos os método criados na classe Livro para os objetos livro1 e livro2.

Elabore o enunciado e a implementação de mais um método funcional na classe Livro.
A complexidade do enunciado e da implementação do método serão considerados para mensurar a avaliação do método.
Obs.: este método deve ser diferente dos métodos vistos nos exemplos usados nas aulas.

        ---[Crie um metodo que muda todos os valores dos atributos de um objeto da classe]---

- Vale 60%

Questão 1:
'''

lista = []              # a)
lista.insert(0, 1)      # a)
while True:
    valores = float(input("Digite valores para a lista (Digite [0] para sair): "))      # a)
    if valores == 0:
        break
    lista.append(valores)

media = sum(lista) / len(lista)      # b)
print("Media dos valores: ", media)

for i in lista:     # c)
    if i < 0:
        print('A porcentagem de numeros negativos na lista eh de {}%'.format(i/len(lista)*-1*100))

del lista[0]    # d) (Enunciado embaixo da questao)
print("Lista com valor removido: ", lista)

'''
Questão 2
'''

class Livro(object):
    def __init__(self, titulo, autor, paginas, preco=0.00):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.preco = preco

    def get_preco(self):
        return self.preco
    def set_preco(self, novo_preco):
        if isinstance(novo_preco, float):
            if novo_preco < 0:
                print("ERRO: Digite um valor válido!")
            else:
                self.preco = novo_preco
        else:
            print("ERRO: Digite um tipo válido!")

    def aumento_preco(self):
        aumento = float(input("Digite o aumento: "))
        self.preco = self.preco + aumento

    def muda_valores(self):     # Questao de criar um método funcional (Enunciado embaixo da questao)
        self.titulo = str(input("Digite o Título: "))
        self.autor = str(input("Digite o nome do(a) Autor(a): "))
        self.paginas = int(input("Digite o número de páginas: "))
        self.preco = float(input("Digite o preço do livro: "))

    def retorna_dados(self):
        dados = f'{self.titulo}, {self.autor}, {self.paginas}, {self.preco}'
        return dados

if __name__ == '__main__':
    livro1 = Livro("Harry Potter", "J.K.Rowling", 100, 29.99)
    livro2 = Livro("Jogos Vorazes", "Suzanne Collins", 150)

    print("Preço do livro 1: ", livro1.get_preco())
    livro1.set_preco(float(input("Digite o novo preco: ")))
    print("Novo preço: ", livro1.get_preco())

    livro1.aumento_preco()
    print("Preço depois do aumento: ", "%.2f" % livro1.get_preco())

    print("Preco do livro 2: ", livro2.get_preco())
    livro2.set_preco(float(input("Digite o novo preço: ")))
    print("Novo preço: ", livro2.get_preco())

    livro2.aumento_preco()
    print("Preço depois do aumento: ", "%.2f" % livro2.get_preco())

    livro1.muda_valores()
    print("Informações do livro: ", livro1.retorna_dados())

    livro2.muda_valores()
    print("Informações do livro: ", livro2.retorna_dados())