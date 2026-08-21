from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    @abstractmethod
    def calcular_bonus(self):
        pass

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor=None):
        if valor is None:
            raise ValueError("Impossivel reajustar o salario desse jeito")
        else:
            if valor >= self.__salario:
                self.__salario = valor
            else:
                raise ValueError("voce nao pode reduzir o salario de um funcionario")


class Engenheiro(Funcionario):




class Gerente(Funcionario):
    pass


class Desenvolvedor(Funcionario):
    pass


class Designer(Funcionario):
    pass
