import hashlib
from rich import print

class Credencial:
    def __init__(self):
        self.senha = None
        self.__hash = None

    def Senha(self, code):
        h = hashlib.sha256(code.encode()).hexdigest()
        self.__hash = h
        self.senha = h

    def validar(self, chave):
        chave_hash = hashlib.sha256(chave.encode()).hexdigest()
        if chave_hash == self.__hash:
            print("Senha correta")
            return True
        else:
            print("senha incorreta")
            return False
