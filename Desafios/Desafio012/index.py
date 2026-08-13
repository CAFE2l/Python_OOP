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
        self.alvo = alvo
        self.forca = forca
        print(f"[bold][red]{self.nome} [/]atacou [blue]{alvo.nome}[/] com [yellow]{golpe}[/] de forca [green]{forca}[/]") 
        dano = int(forca * random.uniform(0.15, 0.95))
        alvo.receber_dano(dano)


    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0

        print(f"[bold][red]{self.nome}[/] recebeu dano de[green] {dano}[/]")

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["SOCAO", "VOADORA", "CHUTE NO SACU"]

    def curar(self):
        cura = random.randint(100, 3000)
        self.vida += cura
        print(f"{self.nome} usou pocao de cura e regenerou {cura} de vida")

class Mago(Personagem):
    def __init__(self,nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["MACUMBA SARAVA", "SOLTA PEIDO E SAI FUBA", "PLIM PLIM"]

    def curar(self):
        cura = random.randint(100, 3000)
        self.vida += cura
        print(f"[bold][cyan]{self.nome}[/] usou [red]macumba[/] e regenerou [green]{cura}[/] de vida[/]")




g1 = Guerreiro("Kratos", 30000)
m1 = Mago("Bruxa do 71", 71000)

m1.atacar(g1, 10000)
g1.atacar(m1, 20000)
m1.curar()