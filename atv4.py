class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class livro(produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor


class eletronico(produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem


p1 = livro('O silencio das águas ', 50.00, "Brittainy C. Cherry")
print(p1.nome, p1.preco, p1.autor)