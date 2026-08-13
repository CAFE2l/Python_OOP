from index import *

from rich import print, inspect

def main():
    t = Termostato()
    try:
        t.temperatura = 11.22
        print(t.ftemperatura)
    except Exception as e:
        print(f"Houve um problema: {e}")

    print(f"A temperatura atual e de {t.ftemperatura}{chr(176)}C ")

if __name__ == "__main__":
    main()
