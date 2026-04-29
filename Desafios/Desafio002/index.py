class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def etiqueta(self):
        return f"Produto: {self.nome} - Preço: R${self.preço:.2f}"


produto1 = Produto("Camiseta", 29.99)
print(produto1.etiqueta())
