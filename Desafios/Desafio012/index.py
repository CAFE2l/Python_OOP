from rich import print, inspect 
from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
    
    @abstractmethod
    def atacar(self):
        dado = [1, 2, 3, 4, 5, 6]
        


    @abstractmethod
    def curar(self):
        pass 


class Guerreiro(Personagem):
    def __init__(self, nome, vida):

    def curar()


class Mago(Personagem):
    def __init__(self, nome, vida):
