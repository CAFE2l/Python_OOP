# print(len("tiraaaaaaa"))
# print(len(["curso", "Python"]))
# print(len({"nome": "Gustavo", "idade": 30}))


# print([1,3, 3] + [1, 2, 3])
from index import *


def main():
    a = Cachorro("Bandido")
    a.emitir_som()

    b = Gato("Frango")
    b.emitir_som()

    c = Pato("Tio Patinhas")
    c.emitir_som()

    d = Galinha("Jao frango")
    d.emitir_som()


    e = Golden("REX")
    e.emitir_som()

    g = Pitbull("T-REX")
    g.emitir_som()

if __name__ == "__main__":
    main()
