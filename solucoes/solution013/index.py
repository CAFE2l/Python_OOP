from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, nasc):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nasc

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if 1920 <= ano <= 2026:
            self._nascimento = ano
        else:
            raise ValueError("Ano de nascimento inválido")

    @property
    def idade(self):
        return 2026 - self._nascimento


    @idade.setter
    def idade(self, ano):
        raise PermissionError("Não é possível alterar a idade diretamente")


class Aluno(Pessoa):
    cursos_oficiais = ["Python", "Java", "C++", "JavaScript"]
    def __init__(self, nome:str, nascimento:int, curso:str):
        super().__init__(nome, nascimento)
        self._curso = None

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso:str):
        pass

    def add_curso(self, curso:str):
        pass
