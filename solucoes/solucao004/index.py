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
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo



c1 = Funcionario(nome="Maria", setor="Admin", cargo="diretora")
inspect(c1)