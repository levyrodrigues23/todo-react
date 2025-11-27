from dataclasses import dataclass

@dataclass
class Jogo:
    titulo: str
    genero: str
    copias: int

    def __str__(self):
        return f"'{self.titulo}' ({self.genero}) - {self.copias} cópias disponíveis"

    def alugar(self):
        if self.copias > 0:
            self.copias -= 1
            return True
        return False

    def devolver(self):
        self.copias += 1
