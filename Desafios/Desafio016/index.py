class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self._altura = altura

    @property
    def base(self):
        if (self._base < 0):
            raise ValueError("Base não pode ser negativa")
        else:
            return self._base


    @base.setter
    def base(self, valor):
        if (valor < 0):
            raise ValueError("Base não pode ser negativa")
        else:
            self._base = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        self._altura = valor

    @property
    def area(self):
        return self._base * self._altura

    @property
    def medidas(self):
        return f"Base: {self._base}, Altura: {self._altura}, Area: {self.area}"

    @medidas.setter
    def medidas(self, valores):
        self.altura, self.base = valores
