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

15-h1- Conceito de herança: eliminar código repetido e herdar atributos e métodos
16- A subclasse Gerente herda da superclasse Funcionario
17- Altere o construtor da subclasse Gerente.
18- Rode a função main com as alterações realizadas.
19-h2- Os funcionários recebem uma bonificação. Todos os funcionários recebem 10% do
    valor do salário.
    Então: crie o método bonificacao, ele não recebe nada e retorna o valor da bonificação.
20- Mostre a bonificacao das instâncias f1 e g1.
21- Use o método __str__ para o gerente instanciado (objeto g1).
22- Dados incompletos. Por quê? Sobrescreva o método __str__ na classe gerente
23- Altere o __str__ na subclasse, aproveite o que tem no __str__ da superclasse.
24- Utilize o método vars() ou __dict__ para acessar os atributos de Funcionario e Gerente.
    Ex.: print(vars(objeto))
25- Crie o método salario_total, ele não recebe nada e retorna o salário total do funcionário,
ou seja o valor do salário mais o valor da boninficação.
26- Use o método salario_total para o objeto f1 e o objeto g1.
27- Os gerentes passaram a receber um bônus extra de 500 reais. Atualize o salário total
28-h3- Crie a segunda subclasse Vendedor com os atributos nome, cpf, salario, valor das vendas,
   porcentagem (8%, 12%, ... )
29- Crie uma instância (objeto) da classe Vendedor e testes os métodos da superclasse.
30- Use o método __str__.
'''

class Funcionario(object):                          # Superclasse ou classe pai
    def __init__(self, cpf, nome, salario=0.0):
        self.cpf = cpf
        self.nome = nome
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
        s = f'Nome: {self.nome}, CPF: {self.cpf}, Salario: {self.salario}'
        return s

    def bonificacao(self):
        return self.salario * 0.10

    def salario_total(self):
        total = self.salario + self.bonificacao()
        return total

class Gerente(Funcionario):
    def __init__(self, cpf, nome, salario, senha, qnt_gerencia=0):
        super().__init__(cpf, nome, salario)
        self.senha = senha
        self.qnt_gerencia = qnt_gerencia

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
        if senha == self.senha:
            print('Acesso permitido.')
            return True
        else:
            print('Acesso negado.')
            return False

    def __str__(self):
        # s = f'Nome: {self.nome}, CPF: {self.cpf}, Salario: {self.salario}, Funcionarios gerenciados: {self.qnt_gerencia}'
        s1 = super().__str__()      # Busca a informação acima da Superclasse
        s = s1 + f', Funcionarios gerenciados: {self.qnt_gerencia}'
        return s

    def salario_total(self):
        print('Gerente')
        # total = self.salario + self.bonificacao() + 500       # Solução 1
        total = super().salario_total() + 500                   # Solucção 2 (usando o metodo super() que recupera da Superclasse)
        return total

class Vendedor(Funcionario):
    def __init__(self, cpf, nome, salario=0.0, valor_vendas=0.0, porcent=0.0):
        super().__init__(cpf, nome, salario)
        self.valor_vendas = valor_vendas
        self.porcent = porcent

    def get_valor_vendas(self):
        return self.valor_vendas
    def set_valor_vendas(self, nv_valor):
        self.valor_vendas = nv_valor

    def get_porcent(self):
        return self.porcent
    def set_porcent(self, nv_porcent):
        self.porcent = nv_porcent

if __name__ == '__main__':
    f1 = Funcionario('123', 'Paulo', 1000.0)
    print(f1)
    print(f'Nome: {f1.get_nome()}')
    print(f'CPF: {f1.get_cpf()}')
    print('Salario: ', f1.get_salario())
    r = f1
    print(r)
    print(f1)

    g1 = Gerente('234', 'Paula', 3000.0, 's1', 5)
    print(f'\nNome: {g1.get_nome()}')
    print(f'CPF: {g1.get_cpf()}')
    print(g1)
    r = g1.autentica()
    if r:
        pass
    print(r)

    # Herança 2
    bonificacao_f1 = f1.bonificacao()                   # Usando uma variavel
    print(f'Bonificação de f1: {bonificacao_f1}')       # Formas equivalentes
    print(f'Bonificação de g1: {g1.bonificacao()}')     # Uso com um objeto da superclasse

    print(vars(f1))                                     # print(vars(objeto))
    print(f1.__dict__)
    print(vars(g1))
    print(g1.__dict__)

    print('Salario total de f1: ', f1.salario_total())
    print('Salario total de g1: ', g1.salario_total())

    # Herança 3
    v1 = Vendedor('223', 'Ailton', 2000.0, 25000.0, 10) # Instancia da subclasse Vendedor
    print('Nome: ', v1.get_nome())
