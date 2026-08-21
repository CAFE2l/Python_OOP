from functools import singledispatchmethod
from rich import print, inspect
from abc import ABC, abstractmethod

class Analisador:
    @singledispatchmethod
    def analisar(self, valor):
        print(f"It was not possible to analyse the value {valor}")

    @analisar.register
    def _(self, valor:int):
        print(f"{valor} its a number")

    @analisar.register
    def _(self, valor:str):
        print(f"{valor} its a string")

    @analisar.register
    def _(self, valor: float):
        print(f"{valor} its a number with a float number")

    @analisar.register
    def _(self, valor: tuple|list|dict):
        print(f"{valor} its a collection of data")
