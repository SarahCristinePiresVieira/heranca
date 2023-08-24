class bebida:
    def __init__(self, nome, tipo):
        self.nome=nome
        self.tipo = tipo

class Refrigerante(bebida):
    def __init__(self,nome, tipo, preco):

        super().__init__(nome, tipo)
        self.preco = preco

class café(bebida):
    def __init__(self,nome, tipo,marca):
        super().__init__(nome, tipo)
        self.marca = marca


b1 = Refrigerante('coca', "zero", 9.99)
b2 = café('café', 'expresso', 'Café Macali')
print(b1.tipo)