from rich import print, inspect
from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome:str, sal_min:float = 1612, inss:float = 7.5):
        self.nome = nome
        self.sal_min = salmin

         
    @abstractmethod
    def calc_sal(self) -> float:
        pass

    @abstractmethod
    def analisar_sal(self) -> float:
        pass

class FuncionarioHorista(Funcionario):
    def __init__(self, valor_hora, horas_trab):
        super().__init__()

    def calc_sal(self)
