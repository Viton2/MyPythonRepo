from pessoa_1 import Pessoa

'''

1- Crie a classe Pessoa
2- Crie o método construtor:
  Ele recebe o self e mais três parâmetros que serão armazenados nos atributos.
  Dentro do construtor, crie os três atributos da classe (nome, sobrenome e idade)
3- No método main, crie o objeto pessoa1 e passe os argumentos "Carlos", "Pereira", 23
4- Mostre o objeto criado, o objeto pessoa1, teste (use a classe)
5- Na classe, crie os métodos get (consultar) e set (alterar) para os atributos nome e idade
   def get_nome_atributo1 (self):

'''

if __name__ == '__main__':                              # Atalho: mai <tab>
    pessoa1 = Pessoa("Carlos", "Pereira", 23)           # Instantiate an object of type Pessoa
    print(pessoa1)                                      # Mostra o objeto pessoa1 da classe Pessoa e seu endereço hexadecimal
    print(pessoa1.__str__())                            # Mostra o objeto pessoa1 da classe Pessoa e seu endereço hexadecimal
    v = pessoa1.get_nome()                              # Usando variável
    print("Nome: ", v)
    print("Idade", pessoa1.get_idade())                 # Sem variável
    novo_nome = input('Novo nome: ')                    # Usa input
    pessoa1.set_nome(novo_nome)
    pessoa1.set_nome('Rogério')                         # Sem input
    print('Nome: ', pessoa1.get_nome())                 # Teste
    pessoa1.set_idade(35)                               # Valor e tipo corretos
    print("Idade: ", pessoa1.get_idade())               # Teste