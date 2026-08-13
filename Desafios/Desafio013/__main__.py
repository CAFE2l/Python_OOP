from index import *

from rich import print, inspect


def main():
    t = Termostato(25)

    inspect(t, private=True, methods=True)

    print(f"A temperatura atual é {t.ftemperatura}")

    t.aumentar()
    print(f"Depois de aumentar: {t.ftemperatura}")

    t.diminuir()
    t.diminuir()
    print(f"Depois de diminuir duas vezes: {t.ftemperatura}")


if __name__ == "__main__":
    main()