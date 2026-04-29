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


class Churrasco:
    def __init__(self, pessoas, carne):
        self.pessoas = pessoas
        self.carne = carne

    def calcular_carne(self):
        if self.carne == "bovina":
            return self.pessoas * 400
        elif self.carne == "suina":
            return self.pessoas * 300
        elif self.carne == "frango":
            return self.pessoas * 200
        else:
            return "Tipo de carne inválido. Use 'bovina', 'suina' ou 'frango'."

    def custo_total(self, preco_por_kg):
        carne_necessaria = self.calcular_carne()
        if isinstance(carne_necessaria, int):
            return carne_necessaria * preco_por_kg / 1000
        else:
            return carne_necessaria

    def preco_por_pessoa(self, preco_por_kg):
        custo_total = self.custo_total(preco_por_kg)
        if isinstance(custo_total, (int, float)):
            return custo_total / self.pessoas
        else:
            return custo_total


churrasco1 = Churrasco(10, "bovina")
preco_por_kg = 30  # Exemplo de preço por kg
print(
    f"{estilos['negrito']}Carne necessária: {cores['vermelho']}{churrasco1.calcular_carne()} gramas{cores['limpa']}"
)

print(
    f"{estilos['negrito']}Custo total: {cores['verde']}R${churrasco1.custo_total(preco_por_kg):.2f}{cores['limpa']}"
)

print(
    f"{estilos['negrito']}Preço por pessoa: {cores['azul']}R${churrasco1.preco_por_pessoa(preco_por_kg):.2f}{cores['limpa']}"
)
