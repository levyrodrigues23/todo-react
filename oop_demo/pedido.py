from typing import List, Dict

from .cliente import Cliente
from .produto import Produto


class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int = 1):
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self) -> float:
        return self.produto.preco * self.quantidade


class Pedido:
    def __init__(self, id: int, cliente: Cliente, itens: List[ItemPedido] = []):
        self.id = id
        self.cliente = cliente
        self.itens = itens
        self.desconto_percentual = 0.0

    def total_bruto(self) -> float:
        total = 0.0
        for it in self.itens:
            total += it.subtotal()
        print(f"DEBUG total_bruto: {total}")
        return total

    def fechar(self) -> Dict[str, object]:
        erros: List[str] = []
        if not self.cliente.email_valido():
            erros.append("Email inválido")
        if not self.itens:
            erros.append("Sem itens")
        if erros:
            return {"ok": False, "erros": erros}

        bruto = self.total_bruto()
        liquido = max(0.0, bruto * (1 - self.desconto_percentual))
        itens_dict = [
            {
                "produto": it.produto.nome,
                "qtd": it.quantidade,
                "subtotal": it.subtotal(),
            }
            for it in self.itens
        ]
        return {
            "ok": True,
            "pedido": self.id,
            "cliente": self.cliente.to_dict(),
            "itens": itens_dict,
            "bruto": bruto,
            "desconto": self.desconto_percentual,
            "liquido": liquido,
        }


