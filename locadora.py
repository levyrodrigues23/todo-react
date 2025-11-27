from jogo import Jogo

class Locadora:
    def __init__(self, nome):
        self.nome = nome
        self.catalogo_jogos = {}

    def __str__(self):
        return self.nome

    def adicionar_jogo(self, jogo: Jogo):
        self.catalogo_jogos[jogo.titulo.lower()] = jogo
        print(f"'{jogo.titulo}' foi adicionado ao catálogo da locadora.")

    def buscar_jogo(self, titulo_jogo):
        return self.catalogo_jogos.get(titulo_jogo.lower())

    def listar_catalogo(self):
        if not self.catalogo_jogos:
            print("O catálogo de jogos está vazio.")
            return

        print(f"--- Catálogo de Jogos da {self.nome} ---")
        for jogo in self.catalogo_jogos.values():
            print(jogo)
        print("-----------------------------------------")
