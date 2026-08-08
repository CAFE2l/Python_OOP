from abc import ABC, abstractmethod


class Bebida(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    def preparar(self) -> None:
        print(f"---- Iniciando o Preparo ----") 
        print(f"1. Fervendo a agua a 100 graus celsius")
        self.misturar()
        self.servir()
        self.final()

    @abstractmethod
    def misturar(self) -> str:
        pass

    @abstractmethod
    def servir(self) -> str:
        pass

    def final(self) -> None:
        print(f"---- Bebida Pronta ----")

    
class Cafe(Bebida):
    def __init__(self):
        super().__init__("Cafe")
        

    def misturar(self) -> None:
        print(f"2. Passando a agua pressurizada pelo po de cafe moido")
        
    def servir(self) -> None:
        print(f"3. Servindo em xicara pequena")

class Cha(Bebida):
    def __init__(self):
        super().__init__("Cha")

    def misturar(self) -> None:
        print("2. Mergulhando o sache de ervas na agua.")

    def servir(self) -> None:
        print("3. Servindo na caneca de porcelana com folhas")
    
class Leite(Bebida):
    def __init__(self):
        super().__init__("Leite")

    def misturar(self) -> None:
            print("2. Passando vapor pressurizado pelo bico do leite")

    def servir(self) -> None:
            print("3. Servindo em xicara grande")

    
