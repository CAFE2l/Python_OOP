import hashlib
from rich import print
import getpass

class ContaBancaria:
    def __init__(self, id, nome, saldo, chave):
        self.id = id
        self._titular = nome
        self.__saldo = float(saldo)
        self.__hash = hashlib.sha256(chave.encode()).hexdigest()

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novo_nome):
        print("senha kiridinho KKKK: ")
        chave_informada = self.pede_senha()
        if self.validar_senha(chave_informada):
            self._titular = novo_nome
            print("[bold][green]Nome atualizado com sucesso![/green][/]")
        else:
            print("[bold][red]Senha incorreta![/red][/]")


    def validar_senha(self, chave: str) -> bool:
        chave_hash = hashlib.sha256(chave.encode()).hexdigest()
        return self.__hash == chave_hash

    def pede_senha(self) -> str:
        return getpass.getpass("Digite sua senha: ")

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print(f"se fodeo kirio KK")

    def sacar(self, valor: float, chave: str = None) -> None:
        if chave is None:
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if 0 < valor <= self.__saldo:
                self.__saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
                return True
            else:
                print(f"se fodeo kirio KK")
                return False
        else:
            print(f"Senha incorreta!")
            return False
