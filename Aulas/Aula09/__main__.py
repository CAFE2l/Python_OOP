from index import *
from rich import print, inspect

def main():
    av1 = Avaliacao("Pedro", "Matematica")
    av1.nota = 9.2
    print(f"{av1.nome} tirou {av1.nota} em {av1.disciplina}")
    inspect(av1, private=True)


if __name__ == "__main__":
    main()