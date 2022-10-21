from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, valor, modelo, km=1, cilindradas=0):
        super().__init__(valor, modelo, km)
        self.cilindradas = cilindradas

    def calcula_ipva(self):
        ipva = self.valor * 0.02
        print(f'IPVA dessa moto: {ipva}')

    def __str__(self):
        s = f'Valor: {self.valor}, Modelo: {self.modelo}, Quilometragem: {self.km}KM, ' \
        f'Cilindradas: {self.cilindradas}'
        return s