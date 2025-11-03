from typing import Dict, Optional, TypeVar, Generic

T = TypeVar("T")


class RepositorioGenerico(Generic[T]):
    def __init__(self):
        self._dados: Dict[int, T] = {}

    def adicionar(self, id: int, entidade: T) -> bool:
        if id in self._dados:
            return False
        self._dados[id] = entidade
        return True

    def obter(self, id: int) -> Optional[T]:
        return self._dados.get(id)

    def remover(self, id: int):
        if id not in self._dados:
            raise KeyError("Inexistente")
        del self._dados[id]


