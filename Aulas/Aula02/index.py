# Declaração de Classe
class Gafanhoto:
    """
    Essa classe representa um gafanhoto, com atributos de nome e idade, e métodos para celebrar aniversário e exibir uma mensagem.
    """

    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."

    def __str__(self):  # Dunder Method
        return f"Gafanhoto(nome={self.nome}, idade={self.idade})"

    def __getstate__(self):
        return f"Estado do Gafanhoto: {self.nome}, {self.idade}"


g1 = Gafanhoto("João", 20)
g1.aniversario()
# print(g1.mensagem())
# print(Gafanhoto.__doc__)  # Dunder Attribute
print(g1)
print(g1.__getstate__())
