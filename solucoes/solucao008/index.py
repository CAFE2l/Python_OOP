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

class Gamer:
    def __init__(self, nome, nick):
        self.nome = input(f"Digite seu {cores['vermelho']}{estilos['negrito']}nome:{cores['cinza']} ")
        self.nick = input(f"Digite seu {cores['azul']}{estilos['negrito']}nick:{cores['cinza']} ")
        self.favoritos = []

    def add_favoritos(self):
        while True:
            jogos = input(f"{estilos['negrito']}Digite seus jogos {cores['amarelo']}favoritos:{cores['cinza']} ") 
            self.favoritos.append(jogos)
            continuar = input(f"Deseja adicionar mais jogos? {cores["verde"]}(s/n):{cores['cinza']} ")
            if continuar.lower() != 's' or continuar.lower() == 'n':
                break

    def status(self):
        print(f"{estilos['negrito']}{cores['vermelho']}Nome: {cores['cinza']}{self.nome}")
        print(f"{estilos['negrito']}{cores['azul']}Nick: {cores['cinza']}{self.nick}")
        print(f"{estilos['negrito']}{cores['amarelo']}Jogos favoritos: {cores['roxo']}{self.favoritos}{cores['limpa']}")

 
j1 = Gamer(nome=None, nick=None)
j1.add_favoritos()
j1.status()