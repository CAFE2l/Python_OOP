from json.encoder import py_encode_basestring_ascii

from rich import print, inspect


class Credencial:
    def __init__(self, senha):
        self.__senha = senha

    def senha(self):
        import hashlib
        return hashlib.sha256(self.__senha.encode()).hexdigest()

    def __str__(self):
        return self.criarSHA256()
