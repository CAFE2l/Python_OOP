from rich import print, inspect
from  abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome:str, sal_min:float = 1612, inss:float = 7.5):
        self.nome = nome
        self.sal_min = sal_min
        self.inss = inss
        self.sal_bruto = 0.0
        self.salrio = 0.0

    @abstractmethod
    def calc_sal(self) -> float:
        pass

    def analisar_sal(self) -> float:
        diferenca = self.salario - self.sal_min

        if diferenca >= 0:
            print("[green][bold]salario acima do salario minimno[/][/]")
        else:
            print("[red][bold] salario abaixo do salario minimo [/][/]")

        return diferenca

class Horista(Funcionario):
    def __init__(self, nome:str, valor_hora:float, horas_trab:float,  sal_min:float=1621, inss:float=7.5) -> float:
        super().__init__(nome, sal_min, inss)
        self.nome = nome 
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        
    def calc_sal(self)-> float:
        self.sal_bruto = self.horas_trab * self.valor_hora
        self.desconto_inss = self.sal_bruto * (self.inss / 100)
        self.salario = self.sal_bruto - self.desconto_inss
        return  self.salario


class Mensalista(Funcionario):
    def __init__(self, nome:str, salario_fixo:float, sal_min:float = 1612, inss:float= 7.5):
        super().__init__(nome, inss, sal_min)
        self.salario_fixo = salario_fixo

    def calc_sal(self) -> float:
        self.sal_bruto = self.salario_fixo
        self.desconto_inss = self.sal_bruto * (self.inss / 100)
        self.salario = self.sal_bruto - self.desconto_inss
        return self.salario



    