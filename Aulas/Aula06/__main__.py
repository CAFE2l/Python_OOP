from classes import Aluno, Funcionario, Pessoa, Professor
from rich import inspect


def main():

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


if __name__ == "__main__":
    main()
