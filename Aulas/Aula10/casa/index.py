class Carteira:
    def __init__(self, valor:int|float = 0):
        self.__saldo = valor

    def __str__(self):
        return f"Voce tem R${self.__saldo} na carteira"


    @property
    def valor(self):
        return self.__saldo

    @valor.setter
    def saldo(self, valor):
        raise PermissionError("You dont have the permission to change the loan on this way")

    def __eq__(self, outro):
        if self.__saldo == outro.__saldo:
            return True
        else:
            return False

    def __iadd__(self, valor:int|float = 0):
        self.__saldo += valor
        return self

    def __isub__(self, valor:int|float):
        self.__saldo = self.__saldo - valor
        return self

    def __le__(self, outro):
        if self.__saldo <= outro.__saldo:
            return True
        else:
            return False
