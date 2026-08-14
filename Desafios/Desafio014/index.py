from rich import print, inspect

class Diario:
    def __init__(self, senha=None):
        self.__segredos = []
        self.__senha = senha

    @property
    def senha(self):
        raise PermissionError("Ninguém tem permissão para ler sem a senha")

    def Escrever(self, texto):
        self.__segredos.append(f"{texto}")


    def Ler(self, senha=None):
        if senha != self.__senha:
            raise PermissionError("[red][bold]Senha incorreta[/][/]")
        elif senha == self.__senha:
            return self.__segredos
        else:
            return f"[red][bold]Assim não filha da puta[/][/]"
