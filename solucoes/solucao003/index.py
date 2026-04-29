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


class ControleRemoto:
    canal_min: int = 1
    canal_max: int = 6
    volume_min: int = 1
    volume_max: int = 5

    def __init__(self, canal: int = 1, volume: int = 2):
        self.canal_atual: int = canal
        self.volume_atual: int = volume
        self.ligado: bool = False

    def toggle_power(self) -> bool:
        """Alterna o estado e devolve o novo estado (True = ligado)."""
        self.ligado = not self.ligado
        return self.ligado

    def mostrar_tv(self) -> str:
        """Retorna a representação textual da TV (quem chamar decide imprimir)."""
        if not self.ligado:
            return f"{cores['vermelho']}{estilos['negrito']}A TV está desligada{estilos['reset']}{cores['limpa']}"

        conteudo = ""
        conteudo += "CANAL = "
        for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
            if canal == self.canal_atual:
                conteudo += f"{cores['verde']}{estilos['negrito']}[{canal}] "
            else:
                conteudo += f"{cores['cinza']}{estilos['negrito']}{canal} "

        conteudo += f"\nVOLUME = "
        for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
            if volume == self.volume_atual:
                conteudo += f"{cores['verde']}{estilos['negrito']}[{volume}] "
            else:
                conteudo += f"{cores['cinza']}{estilos['negrito']}{volume} "

        conteudo += f"{estilos['reset']}{cores['limpa']}"
        return conteudo


# Uso correto:
c = ControleRemoto()
# Alterna para ligado (não use print se não quiser ver o True/False)
estado = c.toggle_power()  # True se agora estiver ligado
print(c.mostrar_tv())  # imprime a visão atual da TV
