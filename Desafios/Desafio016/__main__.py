from index import *
from rich import print, inspect

def main():
    r = Retangulo(8, 4)
    #r.area = 23 -> tem que dar erro
    # r.altura = 23 -> permite
    # r.base = 33 -> permite
    # r.medidas = (9, 3) -> permite

    inspect(r,private = True, methods = True)

if __name__ == "__main__":
    main()
