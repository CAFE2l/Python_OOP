from index import *
from rich import print, inspect

def main():
    cc = ContaBancaria(id=123, nome="Jao", saldo=10000, chave="Gafanhoto")
    cc.depositar(500)
    # quando sacar pedir senha por favor
    cc.sacar(200, chave="Gafanhoto") #tbm permite passar a chave diretamente
    cc.nome ="Manuel" # pedir senha para alterar o nome

    inspect(cc, private=True, methods=True)

if __name__ == "__main__":
    main()
