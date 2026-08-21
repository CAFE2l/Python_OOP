class Porta:
    def abrir(self):
        print(f"Empurra ou puxar a porta")

class Empresa:
    def abrir(self):
        print(f"go to the portal of the entrepeneur with all documentation for open an CNPJ")

class Ovo:
    def abrir(self):
        print(f"Break the egg with a fork and separate the parts in a griller")


class Pedra:
    pass



def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f"encontrie problemas ao tentar abrir o {objeto.__class__.__name__}")
