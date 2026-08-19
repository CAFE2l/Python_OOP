from rich import print, inspect
from index import *

def main():
   c = Credencial()
   c.Senha("test")
   inspect(c, private=True, methods=True)
if __name__ == "__main__":
    main()
