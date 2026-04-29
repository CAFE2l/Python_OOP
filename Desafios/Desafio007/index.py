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


class ControleRemoto:
    def __init__(self, canal, volume, ligado=False):
        self.canal = canal
        self.volume = volume
        self.ligado = ligado

    def aumentar_volume(self):
        volume_anterior = self.volume
        self.volume += 1
        return (
            f"{cores['cinza']}{estilos['negrito']}Volume aumentado de "
            f"{cores['vermelho']}{volume_anterior} "
            f"{cores['cinza']}para {cores['verde']}{self.volume}{cores['limpa']}"
        )

    def diminuir_volume(self):
        volume_anterior = self.volume
        self.volume -= 1
        return (
            f"{cores['cinza']}{estilos['negrito']}Volume diminuído de "
            f"{cores['vermelho']}{volume_anterior} "
            f"{cores['cinza']}para {cores['verde']}{self.volume}{cores['limpa']}"
        )

    def mudar_canal(self, novo_canal):
        canal_anterior = self.canal
        self.canal = novo_canal
        return (
            f"{cores['azul']}Canal alterado de {cores['amarelo']}{canal_anterior} "
            f"{cores['azul']}para {cores['verde']}{self.canal}{cores['limpa']}"
        )

    def ligar(self):
        self.ligado = True
        return f"{cores['verde']}Televisão ligada{cores['limpa']}"

    def desligar(self):
        self.ligado = False
        return f"{cores['vermelho']}Televisão desligada{cores['limpa']}"


controle = ControleRemoto(canal=5, volume=10)
print(controle.ligar())
print(controle.aumentar_volume())
print(controle.diminuir_volume())
print(controle.mudar_canal(10))
print(controle.desligar())
