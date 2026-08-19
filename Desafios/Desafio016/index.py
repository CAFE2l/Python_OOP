class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self._altura = altura

    @property # permitindo getter e setter
    def base(self):
        if (self._base < 0):
            raise ValueError("Base não pode ser negativa")
        else:
            return self._base

    @base.setter
    def base(self, base):
        self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    @property
    def area(self):
        return self._base * self._altura

    @property
    def medidas(self):
        return f"Base: {self._base}\n Altura: {self._altura} \n Area: {self.area}"

    @medidas.setter
    def medidas(self, valores):
        self._base, self._altura = valores
