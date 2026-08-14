from index import *
from rich import inspect, print

def main():
    d = Diario("Gafanhoto")
    d.Escrever("primeira mensagem")
    d.Escrever("Você é uma pessoa muito simpática")
    d.Escrever("Que isso cara")

    d.Ler("Gafanhoto")

    inspect(d, methods=True, private=True)
if __name__ == "__main__":
    main()
