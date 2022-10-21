from veiculo import Veiculo

'''

1- Crie a classe Veiculo
2- Crie o construtor da classe com os atributos: modelo, ano, valor
3- No main, crie pelo menos dois objetos da classe. Teste
4- Crie os métodos gets e sets do atributo modelo. Teste
5- Altere o modelo do veiculo. Teste
6- Altere o valor do veiculo, crie o método set_valor. Teste
7- Faça uma crítica no método set_valor para evitar dados inconsistentes. Teste
8- Crie o método mostra_dados. Ele mostra todos os atributos da classe. Teste
9- Crie o metodo retorna_dados, ele retorna os dados (atributos) concatenados. Teste
10- Crie o metodo aumento_valor. Ele recebe o valor do aumento que será acrescentado ao atributo valor do carro. Teste
11- Peça pro usuário fornecer o valor do aumento do veículo. Teste
12- Altere o contrutor para o usuário instanciar um objeto sem valor, valor default 0.
   Ele fornece somente o modelo e ano. Teste, crie um novo objeto (veiculo) só com o modelo e ano.
13- Crie mais um objeto passando apenas o modelo do veiculo, teste

'''

if __name__ == '__main__':                                       #Atalho: mai <tab>
    carro1 = Veiculo('HB', 2018, 50000.00)                       #Chama o metodo __init__ (construtor)
    carro2 = Veiculo('Corolla', 2019, 90000.00)
    print(carro1)
    print(carro2)
    retorno = carro1.get_modelo()                                #Usa variavel
    print('Modelo:', retorno)
    print('Modelo:', carro2.get_modelo())                        #Direto no print, equivalente as duas anteriores
    carro1.set_modelo('HB20')
    print('Modelo:', carro1.get_modelo())                        #Teste
    print('Valor', carro1.get_valor())
    carro1.set_valor(52000.00)                                   #Altera (Substitui) o valor do objeto carro1
    print('Valor:', carro1.get_valor())                          #Teste
    carro2.set_valor(-62000.00)                                  #Argumento (valor) inconsistente
    print(carro2.get_valor())                                    #Teste
    carro1.mostra_dados()
    carro2.mostra_dados()
    print('Dados concatenados, carro 1:\n', carro1.retorna_dados())
    print('Dados concatenados, carro 2:\n', carro2.retorna_dados())
    carro1.aumento_valor(900.00)                                #Passa o argumento (valor) 900
    print('Novo valor:', carro1.get_valor())                    #Teste
    vl_aumento = float(input("Valor aumento: "))
    carro2.aumento_valor(vl_aumento)                            #Usuario digitou input
    print(carro2.get_valor())                                   #Teste
    carro3 = Veiculo('Honda', 2020)                             #Chama o metodo __init__ (construtor)
    print('Valor carro 3:', carro3.get_valor())                 #Testes
    carro3.mostra_dados()
    print('Dados concatenados, carro 3:\n', carro3.retorna_dados())
    carro4 = Veiculo('Argo')
    carro4.mostra_dados()
    carro1.compara_valor(carro2)                                #Carro1 (self) e carro2 (outro_objeto)
    carro1.compara_valor(carro3)                                #Carro1 (self) e carro3 (outro_objeto)