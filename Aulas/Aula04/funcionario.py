from pessoa import Pessoa, cores, estilos


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(
            f"{cores['azul']}{estilos['negrito']}{self.nome} {cores['cinza']}acabou de bater ponto — cargo: {cores['amarelo']}{self.cargo}{cores['cinza']} setor: {cores['verde']}{self.setor}{estilos['reset']}"
        )
