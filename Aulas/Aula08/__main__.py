from index import *

def main():
    c1 = ContaBancaria(id=111, titular="Maria", saldo=5000)
    c1.depositar(-500)
    c1.sacar(-100)
    c1.__saldo = 0 
    c1._titular = "Pedro" # he allows but dot not touch cause 'consenting adults'
    print(c1)

if __name__ == "__main__":
    main()