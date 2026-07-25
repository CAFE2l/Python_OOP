cores = {
    "limpa": "\033[m",
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "amarelo": "\033[33m",
    "azul": "\033[34m",
    "roxo": "\033[35m",
    "ciano": "\033[36m",
    "cinza": "\033[37m",
    "pretoebranco": "\033[7;30m",
}
from rich import print
from rich import inspect
estilos = {
    "reset": "\033[0m",
    "negrito": "\033[1m",
}

class Funcionario:
    #Atributos de classe
    empresa = "Curso em video"


    def __init__(self, nome, setor, cargo):
        #Atributos de instancia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentacao(self) -> str:
        return f":handshake: Hello I'm [blue][bold]{self.nome}[/bold][/blue] and work as [red][bold]{self.cargo}[/bold][/red] at the stage [green][bold]{self.setor}[/green][/bold] on the company [yellow][bold]{self.__class__.empresa}[/bold][/yellow]"





c1 = Funcionario(nome="Maria", setor="Admin", cargo="diretora")
c1.empresa = "FIAP"

c2 = Funcionario(nome="Pedro", setor="TI", cargo="Programador")
print(c1.apresentacao())
print(c2.apresentacao())

