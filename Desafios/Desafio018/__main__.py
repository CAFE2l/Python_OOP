from index import *
from rich import print, inspect

def main():
    a1 = Aluno(
        nome="Julia Leite", nascimento=2010, curso="TEC"    )
    a1.add_curso("TEC")
    inspect(a1, private=True, methods=True)


if __name__ == "__main__":
    main()
