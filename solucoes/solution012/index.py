import hashlib

class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave):
        if len(chave) > 0:
            self.__hash = hashlib.sha256(chave.encode('utf-8')).hexdigest()
        else:
            raise ValueError("senha invalida")


    def validar(self, chave):
        usuario = hashlib.sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            print("senha confere")
            return True
        else:
            print("senha invalida")
            return False
