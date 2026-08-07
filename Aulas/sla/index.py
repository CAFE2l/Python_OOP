from rich import print, inspect
class Pessoa:
    def __init__(self, nome = "cu de comer rosca", idade=0):
        self.nome = nome
        self.idade = idade
        print(f"{self.idade}")
    def fazer_aniversario(self):
        self.idade += 1
        print(f"{self.nome} its his birthday and he is making: {self.idade} years old")

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        self.curo = curso
        self.turma = turma
        
    def fazer_matricula(self):
        pass
class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        pass
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        self.cargo = cargo
        self.setor = setor
    
    def bater_ponto(self):
        pass

a1 = Aluno(nome= "Joseph", idade= 19, curso= "CS", turma= "T01")
inspect(a1)