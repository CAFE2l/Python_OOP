from rich import print
from rich import panel

class Produto:
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} custa {self.preco:,.2f}"

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(30, ' ')}"
        etiqueta = panel.Panel(conteudo, title="Produto", width=34)
        return etiqueta



p1 = Produto("Red Magic 11 pro", 6_000.00)
p2 = Produto("Notebook Tunado", 8_000.00)
print(p1.etiqueta())