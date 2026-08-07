from rich import print
from rich.panel import Panel



class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 1
    volume_max:int = 5

    def __init__ (self, canal = 1, volume = 1):
        self.canal_atual:int = canal
        self.volume_atual: int = volume
        self.ligado: bool = False

    def liga_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1
    def canal_menos(self):
         if self.ligado:
             if self.canal_atual == ControleRemoto.canal_min:
                 self.canal_atual = ControleRemoto.canal_max
             else:
                 self.canal_atual -= 1


    def volume_mais(self):
         if self.ligado:
             if self.volume_atual == ControleRemoto.volume_max:
                 self.volume_atual += 1 


    def volume_menos(self):
        if self.ligado:
            if self.volume_atual == ControleRemoto.volume_min:
                self.volume_atual = self.volume_atual
            else:
                self.volume_atual -= 1

    def mostrar_tv(self):
        if not self.ligado:
            conteudo = f":prohibited: [red]A TV esta desligada [/red]"

        else:
            conteudo = f"CANAL  = "
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f"[yellow on yellow] {canal} [/] "
                else:
                    conteudo += f" {canal} "
                "\n"
            conteudo += f"\n\nVOLUME = "
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max):
                if volume <= self.volume_atual:
                    conteudo +="[black on cyan] [/]"
                else:
                    conteudo += "[black on white] [/]"
        tv = Panel(conteudo, title="[ TV ]", width = 32)
        print(tv)


c1 = ControleRemoto()
c1.liga_desliga()
c1.canal_mais()
c1.canal_mais()
c1.canal_mais()
c1.canal_mais()
c1.mostrar_tv()
c1.volume_menos()
c1.volume_mais()
c1.volume_mais()
c1.volume_mais()
