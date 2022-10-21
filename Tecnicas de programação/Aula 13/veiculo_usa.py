from veiculo import Veiculo
from veiculo_carro import Carro
from veiculo_moto import Moto

if __name__ == '__main__':
    print(f'Quantidade de veiculos: {Veiculo.get_qtd_veiculo()}\n')
    c1 = Carro(3000, 'Hb20', 30000, 2)
    print(c1)
    print(f'Quantidade de veiculos: {Veiculo.get_qtd_veiculo()}\n')

    c2 = Carro(100000, 'Corolla', 0)
    print(c2)
    print(f'Quantidade de veiculos: {Veiculo.get_qtd_veiculo()}\n')

    c3 = Carro(70000, 'Civic')
    print(c3)
    print(f'Quantidade de veiculos: {Veiculo.get_qtd_veiculo()}\n')

    m1 = Moto(20000, 'Batata', 200, 100)
    # print(m1)         <veiculo_moto.Moto object at 0x0000028210508AF0>
    print(vars(m1))     # Metodos do Python
    print(m1.__dict__)  # Metodos do Python
    print(f'Quantidade de veiculos: {Veiculo.get_qtd_veiculo()}\n')

    m2 = Moto(10000, 'XJ6', 300)
    # print(m2)         <veiculo_moto.Moto object at 0x0000028210508DF0>
    print(vars(m2))     # Metodos do Python
    print(m2.__dict__)  # Metodos do Python
    print(f'Quantidade de veiculos: {Veiculo.get_qtd_veiculo()}\n')

    c1.atualiza_valor(500.50)       # Argumento correto
    c1.atualiza_valor(10000)        # Argumento correto
    c1.atualiza_valor(-1100)        # Argumento incorreto (ERRO)
    c1.atualiza_valor('dadwad')     # Argumento incorreto (ERRO)
    print(c1.get_valor())

    c2.atualiza_valor_pct(10)
    print(c2.get_valor())

    m1.atualiza_valor_pct(20)
    print(m1.get_valor())

    c3.situacao()
    c2.situacao()
    m2.situacao()

    c1.situacao_2()                 # Chama o metodo com objeto da subclasse Carro
    m2.situacao_2()                 # Chama o metodo com objeto da subclasse Moto

    c1.calcula_ipva()
    m2.calcula_ipva()

    print(f'Quantidade de veiculos: {Veiculo.get_qtd_veiculo()}\n')

    Veiculo.mostra_veiculo()        # Usa o metodo de classe mostra_veiculo() que usa metodo __str__

    Veiculo.calcula_ipva()

    Veiculo.mostra_situacao()