from abc import  ABC, abstractmethod
from rich import print, inspect
from typing import override

class Funcionario(ABC):
    def __init__(self, nome, valor):
        self.nome = nome
        self.__salario = valor

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor):
        if valor > self.__salario:
            self.__salario = valor
        else:
            print("vai na onde filho")

    @abstractmethod
    def calcular_bonus(self):
        pass

class Engenheiro(Funcionario):
    @override
    def calcular_bonus(self):
        bonus = self.salario * 0.25
        print(f"{self.nome} receives {bonus} for being a engineer")



class Gerente(Funcionario):
    @override
    def calcular_bonus(self):
        bonus = self.salario * 0.15
        print(f"{self.nome} receives {bonus} for being a manager")


class Desenvolvedor(Funcionario):
    @override
    def calcular_bonus(self):
        bonus = self.salario * 0.10
        print(f"{self.nome} receives {bonus} for being a developer")


class Designer(Funcionario):
    @override
    def calcular_bonus(self):
        bonus = self.salario * 0.08
        print(f"{self.nome} receives {bonus} for being a Desinger")
