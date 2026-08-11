from rich import print, inspect
class Avaliacao:
    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    #Metodos Acessores
    def get_nota(self):
        return self._nota

    def set_nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor  
        else:
            print("[bold][red]Nota Invalida[/][/]")

