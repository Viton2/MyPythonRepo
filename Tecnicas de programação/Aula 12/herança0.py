'''
Teclas de atalho: ctlr + <d> ---> Duplica linha // ctrl + </> --> Comenta linha


1- Crie a classe Funcionario com os atributos cpf, nome e salario
2- Crie o construtor da classe Funcionario def __init___ (self, ...).
3- Crie uma instância (objeto f1) da classe com os dados necessários (f1 = Funcionario ( ... ) )
4- Crie alguns métodos get e set. Teste.
5- Sobrescreva o método __str__. Ele recebe o objeto e retorna os dados do funcionário. Teste.
6- Crie a classe Gerente e o construtor com os atributos cpf, nome, salario, senha e
   quantidade de funcionários que ele gerencia
7- Crie alguns métodos gets e sets. Teste
8- Mostre todos os dados (atributos) do objeto g1 da classe Gerente
9- Crie o método autentica na classe Gerente. Ele recebe o objeto, o usuário digita a senha,
   imprime: "Acesso permitido." ou "Acesso negado." e retorna o valor booleano True ou False.
10- Use o método autentica para o gerente instanciado (objeto g1).
11- Use o método autentica para o funcionario instanciado (objeto f1). Por quê deu erro?
'''



class Funcionario(object):                          # class Funcionario:
    def __init__(self, cpf, nome, salario=0.0):     # Construtor com valor default
        self.cpf = cpf
        self.nome = nome                            # Atributos de instancia
        self.salario = salario

    def get_cpf(self):
        return self.cpf
    def set_cpf(self, nv_cpf):
        self.cpf = nv_cpf

    def get_nome(self):
        return self.nome
    def set_nome(self, nv_nome):
        self.nome = nv_nome

    def get_salario(self):
        return self.salario
    def set_salario(self, nv_salario):
        self.salario = nv_salario

    def __str__(self):
        s = f'Nome: {self.nome}, CPF: {self.cpf}, Salario: {self.salario}'  # f-string
        return s

class Gerente(object):
    def __init__(self, cpf, nome, salario, senha, qnt_gerencia=0):
        self.cpf = cpf
        self.nome = nome
        self.salario = salario
        self.senha = senha
        self.qnt_gerencia = qnt_gerencia

    def get_cpf(self):
        return self.cpf
    def set_cpf(self, nv_cpf):
        self.cpf = nv_cpf

    def get_nome(self):
        return self.nome
    def set_nome(self, nv_nome):
        self.nome = nv_nome

    def get_salario(self):
        return self.salario
    def set_salario(self, nv_salario):
        self.salario = nv_salario

    def get_senha(self):
        return self.senha
    def set_senha(self, nv_senha):
        self.senha = nv_senha

    def get_qnt_gerencia(self):
        return self.qnt_gerencia
    def set_qnt_gerencia(self, qtd_func):
        self.qnt_gerencia = qtd_func

    def autentica(self):
        senha = input('Digite a senha: ')
        if senha == self.senha:                 # A variavel senha só vale dentro do metodo autentica()
            print('Acesso permitido.')
            return True
        else:
            print('Acesso negado.')
            return False



if __name__ == '__main__':
    f1 = Funcionario('123', 'Paulo', 1000.0)            # Cria o objeto f1 e chama o construtor
    print(f1)       # print(f1.__str__())               # Teste
    print(f'Nome: {f1.get_nome()}')
    print(f'CPF: {f1.get_cpf()}')
    print('Salario: ', f1.get_salario())
    r = f1
    print(r)                                            # print(r.__str__())
    print(f1)                                           # print(f1.__str__())

    g1 = Gerente('234', 'Paula', 3000.0, 's1', 5)
    print(f'\nNome: {g1.get_nome()}')
    print(f'CPF: {g1.get_cpf()}')
    print(g1)       # print(g1.__str__())               # O metodo __str__ nao foi alterado na classe Gerente
    r = g1.autentica()                                  # O metodo retorna True ou False
    if r:                                               # if r == True:
        pass
    print(r)
    # r = f1.autentica()   -----> Erro, class Funcionario nao tem o metodo autentica