from rich import print
from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome:str, sal_min:float=1621, inss:float=7.5):
        self.nome = nome
        self. sal_min = sal_min 
        self.inss = inss
        self.sal_bruto = 0.0
        self.salario = 0.0

    @abstractmethod
    def calc_sal():
        pass

    def analisar_sal(self):
        if self.salario > self.sal_min:
            print("[green][bold] Your salary is bigger than the min salary[/][/]")
        else:
            print("[red][bold] Your salary is less than the min salary[/][/]")



class Horista(Funcionario):
    def __init__(self, nome:str, valor_hora:float, horas_trab:float, sal_min:float=1621, inss:float=7.5):
        super().__init__(nome, sal_min, inss)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.sal_bruto = self.horas_trab * self.valor_hora
        self.desconto_inss = self.sal_bruto * (self.inss/100)
        self.salario = self.sal_bruto - self.desconto_inss
        return self.salario


class Mensalista(Funcionario):
    def __init__(self, nome:str,sal_fixo:float, sal_min:float=1621, inss:float=7.5):
        super().__init__(nome, sal_min, inss)
        self.sal_fixo = sal_fixo


    def calc_sal(self):
        self.sal_bruto = self.sal_fixo
        self.desconto_inss = self.sal_bruto * (self.inss/100)
        self.salario = self.sal_bruto - self.desconto_inss
        return self.salario 




