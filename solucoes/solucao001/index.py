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
    consumo_padrao = 0.400
    preco_por_kg = 80

    def __init__(self, titulo, qtd):
        # atributos de instancia
        self.titulo = titulo
        self.participantes = qtd

    def __str__(self):
        return f"{cores['cinza']}{estilos['negrito']}Esse é o {cores['vermelho']}{self.titulo} {cores['cinza']}com {cores['azul']}{self.participantes} {cores['cinza']}participantes{estilos['reset']}"

    def calcular_quantidade_carne(self) -> float:
        return self.participantes * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_quantidade_carne() * Churrasco.preco_por_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"{cores['cinza']}{estilos['negrito']} Analisando  o {self.titulo} {cores['cinza']}com {cores['azul']}{self.participantes} {cores['cinza']}participantes{estilos['reset']}"
        conteudo += f"Cada Participante comerá {Churrasco.consumo_padrao} Kg e cad KG custa R$ {Churrasco.preco_por_kg:,.2f}"
        conteudo += f"{cores['cinza']}{estilos['negrito']} recomendo comprar {cores['vermelho']}{self.calcular_quantidade_carne()} KG de carne{cores['limpa']}"
        conteudo += f"{cores['cinza']}{estilos['negrito']} o custo total será de {cores['verde']}R${self.calcular_custo_total():,.2f}{cores['limpa']} para participar"
        conteudo += f"{cores['cinza']}{estilos['negrito']} o custo individual será de {cores['amarelo']}R${self.calcular_custo_individual():,.2f}{cores['limpa']} por pessoa"
        return conteudo


cc1 = Churrasco(titulo="Churras dos amigos", qtd=10)
print(cc1)
print(cc1.analisar())
