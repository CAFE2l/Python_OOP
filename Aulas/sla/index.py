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
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
        
    def fazer_matricula(self):
        print(f"{self.nome}acabou de fazer matricula")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"Prof. {self.nome} start taking classes")



class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
    
    def bater_ponto(self):
        print(f"{self.nome} acabou de bater ponto")


a1 = Aluno(nome= "Joseph", idade= 19, curso= "CS", turma= "T01")
a1.fazer_aniversario()
a1.fazer_matricula()
#inspect(a1, methods=True)

p1 = Professor("Noslen", 37, "Portugues", "Mestre")
p1.fazer_aniversario()
p1.dar_aula()

f1 = Funcionario("Miguel", 22, "Zelador", "Limpeza")
f1.fazer_aniversario()
f1.bater_ponto()
