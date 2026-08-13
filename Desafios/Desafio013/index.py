from rich import print, inspect

class Termostato: 
    MIN_TEMP = 16
    MAX_TEMP = 30 
    INCREMENTO = 0.5

    def __init__(self, temperatura=25):
        self.__temperatura = None
        self.temperatura = temperatura

    
    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if not (self.MIN_TEMP <= valor <= self.MAX_TEMP):
            raise ValueError(f"A temperatura deve estar entre {self.MIN_TEMP} e {self.MAX_TEMP}")
    
        valor_ajustado = round(valor/self.INCREMENTO) * self.INCREMENTO
        if valor_ajustado == int(valor_ajustado):
            valor_ajustado = int(valor_ajustado)
        self.__temperatura = valor_ajustado

    def aumentar(self):
        nova_temp = self.temperatura + self.INCREMENTO
        if nova_temp > self.MAX_TEMP:
            print("Temperatura maxima atingida")
        return 
        self.temperatura = nova_temp


    def diminuir(self):
        nova_temp = self.temperatura - self.INCREMENTO
        if nova_temp < self.MIN_TEMP:
            print("Temperatura minima atingida")
        return  
        self.temperatura = nova_temp

    def ftemperatura(self):
        return f"{self.temperatura}C"

