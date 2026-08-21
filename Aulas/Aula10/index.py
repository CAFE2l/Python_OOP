from abc import ABC, abstractmethod
from rich import print, inspect
class Animal(ABC):
    def __init__(self, nome:str=""):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        print(f"{self.nome} is a {self.__class__.__name__} and his/her is making a sound")


class Pato(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer 'cade minha grana FDP'")



class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer au au au!")


class Pitbull(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer 'RUF RUF!' ")


class Golden(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer 'AU UA UA UAU!!!!'")


class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer 'MIAU MIAU!'")


class Galinha(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer 'sou la do frio de janeiro la do brazil'")
