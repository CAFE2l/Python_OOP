from pessoa import Pessoa, cores, estilos


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(
            f"{cores['cinza']}{estilos['negrito']}O aluno {cores['vermelho']}{self.nome}{cores['cinza']} acabou de fazer a matrícula no curso {cores['verde']}{self.curso}{cores['cinza']} turma {cores['amarelo']}{self.turma}{estilos['reset']}"
        )
