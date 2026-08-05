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

class Caneta:
    def __init__(self, cor="azul"):
        self.estado = False  # False = tampada, True = destampada
        self.cor = cor
        print("Escolha a cor da caneta: 1) Azul | 2) Vermelho | 3) Verde")

        opcoes = {1: "azul", 2: "vermelho", 3: "verde"}
        try:
            escolha = int(input("Digite o numero da cor: "))
            self.cor = opcoes.get(escolha, "cinza")
        except ValueError:
            self.cor = "cinza"
            print("Entrada inválida. Definido como cinza por padrão.")

    def tampar(self):
        self.estado = False
        print(estilos["negrito"] + "A caneta está tampada." + estilos["reset"])

    def destampar(self):
        self.estado = True
        print(estilos["negrito"] + "A caneta está destampada." + estilos["reset"])

    def escrever(self, msg):
        if not self.estado:
            print(f"{cores['vermelho']}Erro: A caneta está tampada! Não é possível escrever.{estilos['reset']}")
            return

        cor_codigo = cores.get(self.cor, cores["cinza"])
        print(f"{cor_codigo}{msg}{estilos['reset']}")

    def quebrar_linha(self):
        print()


# Criando instâncias e testando
c1 = Caneta()
c1.escrever("Teste com a caneta tampada")  # -> Erro

c1.destampar() # -> action of destampar the pen
c1.escrever("Olá, agora a caneta está destampada e funcionando!") # -> escrita funciona
c1.quebrar_linha()
c1.escrever("Segunda linha após a quebra.") # -> funciona

c1.tampar()
c1.escrever("Tentando escrever tampada novamente.")
