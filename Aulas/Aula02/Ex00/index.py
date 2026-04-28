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


class ContaBancaria:
    """
    Classe que representa uma conta bancária e permite fazer saques e depósitos
    """

    def __init__(self, id, titular, saldo=0.0):
        self.id = id
        self.titular = titular
        self.saldo = saldo
        print(
            f"{estilos['negrito']}{cores['cinza']}Conta {cores['azul']}{self.id}{cores['cinza']} criada para {cores['vermelho']}{self.titular} {cores['cinza']}com saldo inicial de {cores['verde']}R${self.saldo:.2f}{cores['limpa']}"
        )

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem o saldo de R${self.saldo:.2f}"

    def depositar(self, valor):
        self.saldo += valor
        print(
            f"{cores['cinza']}{estilos['negrito']}Depósito de {cores['verde']}R${valor:.2f} realizado com sucesso.{cores['cinza']} Novo saldo: R${self.saldo:.2f}{cores['limpa']}"
        )

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(
                f"{cores['cinza']}{estilos['negrito']}Saque de {cores['vermelho']}R${valor:.2f} realizado com sucesso.{cores['cinza']} Novo saldo: R${self.saldo:.2f}{cores['limpa']}"
            )
        else:
            print(
                f"{cores['cinza']}{estilos['negrito']}Saldo insuficiente para realizar o saque de {cores['vermelho']}R${valor:.2f}.{cores['cinza']} Saldo atual: R${self.saldo:.2f}{cores['limpa']}"
            )


c1 = ContaBancaria(112, "Gustavo", 3000.0)
c1.depositar(500.0)
print(c1)
print(c1)
c1.sacar(1000000.0)
print(c1)
