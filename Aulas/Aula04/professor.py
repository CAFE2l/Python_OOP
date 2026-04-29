from pessoa import Pessoa, cores, estilos


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(
            f"{cores['verde']}{estilos['negrito']}Prof. {self.nome}{cores['cinza']} começou a dar aula de {cores['amarelo']}{self.especialidade}{cores['cinza']} — nível: {cores['roxo']}{self.nivel}{estilos['reset']}"
        )
