from index import * 

def main():
    p1 = Guerreiro("Kratos", 2000)
    p2 = Mago("bruxa do 71", 300)


    p1.atacar(p2, 1000) 
    p2.curar()
    p2.atacar(p1, 100)

if __name__ == "__main__":
    main()