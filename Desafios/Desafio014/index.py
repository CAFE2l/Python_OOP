from rich import print, inspect

class Diario:
    def __init__(self, senha=None):
        self.__segredos = []
        self.__senha = senha

    @property
    def senha(self):
        raise PermissionError("Senha não definida")

    def Escrever(self, msg):
        self.__segredos.append(msg)


    def Ler(self, senha=None):
        if senha == self.__senha:
            for segredo in self.__segredos:
                print(segredo)
        else:
            raise PermissionError("Senha incorreta")
