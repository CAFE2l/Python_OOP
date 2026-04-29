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

fundo = {
    "branco": "\033[40m",
    "vermelho": "\033[41m",
    "verde": "\033[42m",
    "amarelo": "\033[43m",
    "azul": "\033[44m",
    "roxo": "\033[45m",
    "ciano": "\033[46m",
    "cinza": "\033[47m",
    "vermelho_claro": "\033[101m",
    "verde_claro": "\033[102m",
    "amarelo_claro": "\033[103m",
    "azul_claro": "\033[104m",
    "roxo_claro": "\033[105m",
    "ciano_claro": "\033[106m",
    "cinza_claro": "\033[107m",
}

estilos = {
    "reset": "\033[0m",
    "negrito": "\033[1m",
    "fraco": "\033[2m",
    "italico": "\033[3m",
    "sublinhado": "\033[4m",
    "inverso": "\033[7m",
    "invisivel": "\033[8m",
    "tachado": "\033[9m",
    "duplosublinhado": "\033[21m",
    "normal": "\033[22m",
    "semitalico": "\033[23m",
    "sem_sublinhado": "\033[24m",
    "sem_inverso": "\033[27m",
    "visivel": "\033[28m",
    "sem_tachado": "\033[29m",
}


class Caneta:
    def __init__(self, cor="azul"):
        match cor.lower().strip():
            case "azul":
                escolha = "azul"
            case "vermelho" | "vermelha":
                escolha = "vermelho"
            case "verde":
                escolha = "verde"
            case "amarelo":
                escolha = "amarelo"
            case _:
                pass

        self.cor = cor
        self.tampada = True

    def escrever(self, msg):
        if self.tampada:
            print(
                f"{cores['vermelho']}A caneta está tampada! Destampe para escrever.{estilos['reset']}"
            )
        else:
            print(f"{cores[self.cor]}{msg}{estilos['reset']}")

    def quebrar_linha(self, qtd=1):
        print("\n" * qtd, end="")

    def destampar(self):
        if self.tampada:
            self.tampada = False


c1 = Caneta("azul")
c2 = Caneta("vermelho")
c3 = Caneta("verde")


c1.destampar()
c2.destampar()
c3.destampar()


c1.escrever("Caneta azul azul caneta")
c1.quebrar_linha()
c2.escrever("Caneta vermelha vermelha caneta")
c2.quebrar_linha()
c3.escrever("Caneta verde verde caneta")
c3.quebrar_linha()
