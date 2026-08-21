from index import *

def main():
    c1 = Carteira(2000)
    c2 = Carteira(2000)

    print(c1 == c2)

    if (c1 == c2):
        print("u guys have the same amount in the box")
    else:
        print("the boxes have different values")


if __name__ == "__main__":
    main()
