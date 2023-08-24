class veiculo:
    def __init__(self,  marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class carro(veiculo):
    def __init__(self,marca, modelo, ano, portas):

        super().__init__(marca, modelo, ano)
        self.portas = portas

class moto(veiculo):
    def __init__(self,marca, modelo, ano, rodas):

        super().__init__(marca, modelo, ano)
        self.rodas = rodas

v1 = carro('citroen', "c3", 2023, 4)
print(v1.marca)