from abc import ABC, abstractmethod
import math
from rich import print, inspect

class Poligono:
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self) -> float:
        pass
    
    @abstractmethod
    def area(self) -> float:
        pass

class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(qtd_lados=4)
        self.lado = lado

    def perimetro(self) -> float:
        return self.lado * 4

    def area(self) -> float:
        return self.lado ** 2

class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(qtd_lados=0)
        self.raio = raio
        
    def perimetro(self) -> float:
        return 2 * math.pi * self.raio


    def area(self) -> float:
        return math.pi * (self.raio ** 2)




