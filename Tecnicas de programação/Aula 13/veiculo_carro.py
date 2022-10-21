from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, valor, modelo, km=1, qtd_portas=4):
        super().__init__(valor, modelo, km)
        self.portas = qtd_portas

    def get_portas(self):
        return self.portas
    def set_portas(self, nv_port):
        self.portas = nv_port

    def __str__(self):
        s = f'Valor: {self.valor}, Modelo: {self.modelo}, Quilometragem: {self.km}KM, ' \
        f'Portas: {self.portas}'
        return s

    def calcula_ipva(self):
        ipva = self.valor * 0.03 + 100
        print(f'IPVA desse carro: {ipva}')