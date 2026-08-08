from abc import ABC, abstractmethod
from rich import print, inspect 
#from rich.table import table
class Transporte(ABC):  
    def __init__(self, distancia:float):
        self.distancia = distancia 
        self.frete = 0.0

    @abstractmethod
    def calc_frete(self) -> float:
        pass

    
class Moto(Transporte):
    def __init__(self, distancia:float):
        super().__init__(distancia)
        self.fator = 0.50

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        return f"The price of the income for [bold][yellow]Motorcycles[/][/] are [green][bold]R${self.frete:.1f}[/bold][/green]"



class Carreta(Transporte):
    def __init__(self, distancia:float):
        super().__init__(distancia)
        self.fator = 1.20

    def calc_frete(self):
        if self.distancia < 50:
            return "[red][bold][italic]proibido ter menos de 50km para carretas[/][/][/]"
        else:
            self.frete = self.distancia * self.fator
            return f"The price of the income for [blue][bold]trucks[/][/] are [green][bold]R${self.frete:.1f}[/bold][/green]"


class Van(Transporte):
    def __init__(self, distancia:float):
        super().__init__(distancia)
        self.fator = 1.50

    def calc_frete(self):
        if self.distancia > 25:
            return "[red][bold][italic]proibido ter mais de 25km para van[/][/]"
        else:
            self.frete = self.distancia * self.fator
            return f"The price of the income for [purple][bold]Vans[/][/] are [green][bold]R${self.frete:.1f}[/bold][/green]"

