from rich import print
from rich.panel  import Panel

class Churrasco:
    # Atributos de Classe

    consumo_padrao:float = 0.500 # cada pessoa em media 400 gramas de carne
    preco_kg:float = 50.00

    def __init__(self, titulo, qtd):
        self.titulo = titulo
        self.participantes = qtd

    def __str__(self):
        return f"This is {self.titulo} com {self.participantes} pessoas participando."
    
    def calcular_qtd_carne(self):
        total = self.participantes * self.consumo_padrao
        return total
    def calcular_custo_total(self):
        return self.calcular_qtd_carne() * self.preco_kg

    def calcular_custo_individual(self):
        return self.calcular_custo_total() / self.participantes if self.participantes > 0 else 0

    def analisar(self):
        conteudo = f"Analisando [bold]{self.titulo}[/bold] com {self.participantes} convidados"

        conteudo += f"\nCada Participante will eat {Churrasco.consumo_padrao} Kg"
        conteudo += f"\nTotal de Carne: [bold][red]{self.calcular_qtd_carne():.2f} Kg[/bold][/red]"
        conteudo += f"\n Custo total: [bold][blue]{self.calcular_custo_total():.2f}[/blue][/bold]"
        conteudo += f"\n Custo individual: {self.calcular_custo_individual():.2f}"
        painel = Panel(conteudo.center(30), title=self.titulo)
        print(painel)



c1 = Churrasco("Alerta de Resenha", qtd=10)
c1.analisar()

c2 = Churrasco("Festade fim de ano", qtd = 20)
c2.analisar()