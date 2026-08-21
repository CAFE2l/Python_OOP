from abc import ABC, abstractmethod
from typing import override
from rich import print, inspect

class Mae:
    def __init__(self, nome:str = "Djabo"):
        self.nome = nome

    def fazer_pudim(self):
        print(f"{self.nome} faz pudim com leite condensado e calda.")

    def fritar_coxinha(self):
        print(f"{self.nome} frita coxinha no oleo de soja")



class Filha(Mae):
    def fazer_pudim(self):
        print(f"{self.nome} faz PUDIM com leite Ninho com Nutella")

class Filho(Mae):
    @override
    def fritar_coxinha(self):
        print(f"{self.nome} frita COXINHA na Air Fryer")
