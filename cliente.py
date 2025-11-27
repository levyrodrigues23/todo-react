from jogo import Jogo

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.jogos_alugados = []

    def __str__(self):
        return self.nome

    def alugar_jogo(self, jogo: Jogo):
        if jogo.alugar():
            self.jogos_alugados.append(jogo)
            print(f"{self.nome} alugou '{jogo.titulo}'.")
            return True
        else:
            print(f"Desculpe, '{jogo.titulo}' não está disponível no momento.")
            return False

    def devolver_jogo(self, jogo: Jogo):
        if jogo in self.jogos_alugados:
            jogo.devolver()
            self.jogos_alugados.remove(jogo)
            print(f"{self.nome} devolveu '{jogo.titulo}'.")
        else:
            print(f"Erro: {self.nome} não alugou '{jogo.titulo}'.")

    def listar_jogos_alugados(self):
        if not self.jogos_alugados:
            print(f"{self.nome} não tem jogos alugados.")
            return

        print(f"Jogos alugados por {self.nome}:")
        for jogo in self.jogos_alugados:
            print(f"- {jogo.titulo}")
