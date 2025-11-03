from typing import List, Dict

from .cliente import Cliente
from .produto import Produto
from .pedido import Pedido, ItemPedido
from .repositorio import RepositorioGenerico


class ServicoPedidos:
    def __init__(self, repo_clientes: RepositorioGenerico[Cliente], repo_produtos: RepositorioGenerico[Produto]):
        self.repo_clientes = repo_clientes
        self.repo_produtos = repo_produtos

    def criar_e_fechar_pedido(self, cliente_id: int, itens_info: List[Dict[str, int]], desconto: float = 0.0) -> Dict[str, object]:
        cliente = self.repo_clientes.obter(cliente_id)
        if not cliente:
            return {"ok": False, "erro": "Cliente inexistente"}

        itens: List[ItemPedido] = []
        for info in itens_info:
            prod = self.repo_produtos.obter(info.get("produto_id", -1))
            if not prod:
                continue
            itens.append(ItemPedido(produto=prod, quantidade=info.get("quantidade", 1)))

        pedido = Pedido(id=cliente_id * 1000, cliente=cliente, itens=itens)
        pedido.desconto_percentual = desconto
        resultado = pedido.fechar()

        if resultado.get("ok"):
            resultado["resumo"] = f"Pedido {resultado['pedido']} de {cliente.nome} com {len(itens)} item(ns)"
        return resultado


