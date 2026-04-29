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
        self.cor = cor

    def escrever(self):
        print("(1) Azul (2) Vermelho (3) Verde (4) Amarelo")
        resposta = int(input("Digite a cor que deseja utilizar: "))
        frase = input("Digite a frase que deseja escrever: ")

        mapa_opcoes = {
            1: "azul",
            2: "vermelho",
            3: "verde",
            4: "amarelo",
        }

        mapa_cores = {
            "azul": cores["azul"],
            "vermelho": cores["vermelho"],
            "verde": cores["verde"],
            "amarelo": cores["amarelo"],
        }

        if resposta not in mapa_opcoes:
            return "Opção inválida"

        self.cor = mapa_opcoes[resposta]
        return f"{mapa_cores[self.cor]}{frase}{estilos['reset']}"


test = Caneta()
print(test.escrever())
