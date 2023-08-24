class Pessoa:
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade

class Aluno(Pessoa):
    def __init__(self,nome,idade,matricula):

        super().__init__(nome,idade)
        self.matricula = matricula

Sarah = Aluno('Sarah', 16, "matriculada")
print(Sarah.matricula)