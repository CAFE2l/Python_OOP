from abc import ABC, abstractmethod
from rich import print


class Pessoa(ABC):
    def __init__(self, nome, nascimento, idade = None):
        self._nome = nome
        self._nascimento = nascimento
        self._idade = idade

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self._nascimento = nascimento

    @property
    def idade(self):
        if self._idade is None:
            self._idade = 2026 - self._nascimento
        elif self._nascimento > 2026:
            return "Idade inválida"
        elif self._nascimento < 1920:
            return "Idade inválida"
        return self._idade

class Aluno(Pessoa):
    def __init__(self, nome, nascimento, curso, idade=None, cursos_oficiais=None):
        super().__init__(nome, nascimento, idade)
        self.cursos_oficiais = ["ADM", "KKK", "EPTEC", "EAD"]
        self._curso = curso

    @property
    def curso(self):
        if self._curso not in self.cursos_oficiais:
            return "Curso inválido"
        return self._curso

    def add_curso(self, curso):
        self.cursos_oficiais.append(curso)
