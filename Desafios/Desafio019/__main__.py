from index import *

def main():
     james = Engenheiro("James Scholz", 18000)
     james.calcular_bonus()
     james.salario = 200
     print(calcular_bonus())

if __name__ == "__main__":
    main()
