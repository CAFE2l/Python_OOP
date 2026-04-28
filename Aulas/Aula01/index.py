# Declaração de Classe
class Gafanhoto:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."


g1 = Gafanhoto()
g1.nome = "CAFE"
g1.idade = 16
g1.aniversario()

g2 = Gafanhoto()
g2.nome = "JOAO"
g2.idade = 20
g2.aniversario()
print(g1.mensagem(), g2.mensagem())
