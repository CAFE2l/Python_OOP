from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min: int = 1
    canal_max: int = 5
    volume_min: int = 0 
    volume_max: int = 5

    def __init__(self, canal: int, volume_atual: int):
        self.canal_atual: int = canal
        self.volume: int = volume_atual
        self.ligado: bool = False

    def mostrar_tv(self):
        if not self.ligado:
            conteudo = "A TV is turned off"
        else:
            conteudo = f"Canal: {self.canal_atual} | Volume: {self.volume}"

        # Criamos o painel e o exibimos diretamente com o print do rich
        painel = Panel(conteudo, title="[ TV ]")
        print(painel)

# Passando os valores iniciais obrigatórios (ex: canal 3, volume 2)
tv = ControleRemoto(canal=3, volume_atual=2)

# Testando com a TV desligada
tv.mostrar_tv()

# Ligando a TV e testando novamente
tv.ligado = True
tv.mostrar_tv()
