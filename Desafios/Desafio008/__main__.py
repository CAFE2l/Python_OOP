from rich import print, inspect 
from index import *

def main():
    p1 = Quadrado(20)

    print(f"Perimetro = {p1.perimetro():.1f}")
    print(f"Area = {p1.area():.1f}")
     
if __name__ == "__main__":
    main()