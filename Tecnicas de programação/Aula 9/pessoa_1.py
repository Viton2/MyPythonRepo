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


class Pessoa(object):  # Por convenção, nome de classe começa cada palavra com letra maiúscula
    def __init__(self, nome, sobrenome, idade):  # Método construtor
        self.nome = nome  # Atributos
        self.sobrenome = sobrenome
        self.idade = idade

    def get_nome(self):
        return self.nome

    def set_nome(self, p_nome):
        self.nome = p_nome

    def get_idade(self):
        return self.idade

    def set_idade(self, id):  # Com crítica
        # if type(id) == int:                                # Dois if equivalentes
        if isinstance(id, int):
            if id >= 0 and id <= 140:
                self.idade = id
            else:
                print("Erro: Idade Inválida.")
        else:
            print("Erro: Tipo Inválido.")
