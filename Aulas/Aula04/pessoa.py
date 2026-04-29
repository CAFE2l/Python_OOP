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

estilos = {
    "reset": "\033[0m",
    "negrito": "\033[1m",
}


class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
        print(
            f"{cores['cinza']}{estilos['negrito']}Parabéns {cores['azul']}{self.nome} {cores['cinza']}você agora tem {cores['verde']}{self.idade} {cores['cinza']}anos{estilos['reset']}"
        )
