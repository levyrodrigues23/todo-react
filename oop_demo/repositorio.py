class RepositorioGenerico:
    def __init__(self):
        self._dados = {}

    def adicionar(self, id, entidade):
        if id in self._dados:
            return False
        self._dados[id] = entidade
        return True

    def obter(self, id):
        return self._dados.get(id)

    def remover(self, id):
        if id not in self._dados:
            raise KeyError("Inexistente")
        del self._dados[id]


