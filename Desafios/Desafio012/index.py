from rich import print
from abc import ABC, abstractmethod
import random


class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca):
        golpe = random.choice(self.golpes)
        print(f"{self.nome} Atacou {alvo.nome} com forca de {forca}")

        dano = int(forca * random.uniform(0.15, 0.95))
        alvo.receber_dano(dano)


    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            print(f"[bold][italic][red]ESTA NO CEMITERIO[/][/][/]")
        else:
            print(f"{self.nome} recebeu dano de {dano}")
    

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["SOCAO", "VOADORA", "CHUTE NO SACU", "FORA ZOIO", "PUXA TETA"]

    def curar(self):
        cura = random.randint(1000, 5000)
        self.vida += cura
        print(f"{self.nome} usou pocao e regenerou {cura} de vida")


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["MACUMBA SARAVA", "MAGIA PRETA", "BRUXARIA"]
        
    def curar(self):
        cura = random.randint(1000, 5000)
        self.vida += cura
        print(f"{self.nome} FEZ FEITICARIA e regenrou {cura} de vida")

    

