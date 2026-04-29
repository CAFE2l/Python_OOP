from rich import inspect, print

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


class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
        return f"{cores['cinza']}{estilos['negrito']}Parabéns {cores['azul']}{self.nome} {cores['cinza']}você agora tem {cores['verde']}{self.idade} {cores['cinza']}anos{estilos['reset']}"


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(
            f"{cores['cinza']}{estilos['negrito']}O aluno {cores['vermelho']}{self.nome}{cores['cinza']} acabou de fazer a matricula"
        )


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(
            f"{cores['verde']}{estilos['negrito']}Prof. {self.nome}{cores['cinza']} começou a dar aula"
        )


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(
            f"{cores['azul']}{estilos['negrito']} {self.nome} {cores['cinza']}acabou de bater ponto"
        )


a1 = Aluno("Jose", 20, "Python", "A")
a1.fazer_matricula()
a1.fazer_aniversario()
inspect(a1, methods=True)

p1 = Professor("anderson", 31, "PHP", "senior")
p1.dar_aula()
inspect(p1)

f1 = Funcionario("isaac", 16, "estágiario", "TI")
f1.bater_ponto()
inspect(f1)
