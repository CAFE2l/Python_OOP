from index import *

def main():
    c = Credencial()
    c.senha = 'CEV!@'
    print(c.senha)
    c.validar('Guanabara')
    c.validar('CEV!@')

if __name__ == "__main__":
    main()
