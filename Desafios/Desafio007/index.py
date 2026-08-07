from rich import print
from rich.panel import Panel

class ControleRemoto: 
    volume_max:int = 4
    volume_min:int = 0
    canal_max:int = 5
    canal_min: int = 1
    def __init__(self, canal=0, volume_atual=0):
        self.canal_atual = canal
        self.volume = volume_atual
        self.ligado: bool = False

    def mostrar_tv(self):
        conteudo = ""
        if not self.ligado:
            conteudo = "The tv is not turn it on"
        else:

