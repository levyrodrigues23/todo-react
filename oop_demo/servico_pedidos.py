class ServicoPedidos:
    def __init__(self, repo_clientes, repo_produtos):
        self.repo_clientes = repo_clientes
        self.repo_produtos = repo_produtos

    def criar_e_fechar_pedido(self, cliente_id, itens_info, desconto=0.0):
        cliente = self.repo_clientes.obter(cliente_id)
        if not cliente:
            return {"ok": False, "erro": "Cliente inexistente"}

        itens = []
        for info in itens_info:
            prod = self.repo_produtos.obter(info.get("produto_id", -1))
            if not prod:
                continue
            itens.append({"produto": prod, "quantidade": info.get("quantidade", 1)})

        # Construção manual do pedido reduzida para não depender de importações
        pedido = type("Pedido", (), {})()
        pedido.id = cliente_id * 1000
        pedido.cliente = cliente
        pedido.itens = [
            type("ItemPedido", (), {"produto": it["produto"], "quantidade": it["quantidade"], "subtotal": lambda self=it: it["produto"].preco * it["quantidade"]})()
            for it in itens
        ]
        pedido.desconto_percentual = desconto

        def total_bruto_local():
            total = 0.0
            for it in pedido.itens:
                total += it.subtotal()
            return total

        erros = []
        if not cliente.email_valido():
            erros.append("Email inválido")
        if not pedido.itens:
            erros.append("Sem itens")
        if erros:
            return {"ok": False, "erros": erros}

        bruto = total_bruto_local()
        liquido = max(0.0, bruto * (1 - pedido.desconto_percentual))
        itens_dict = [
            {
                "produto": it.produto.nome,
                "qtd": it.quantidade,
                "subtotal": it.subtotal(),
            }
            for it in pedido.itens
        ]
        return {
            "ok": True,
            "pedido": pedido.id,
            "cliente": cliente.to_dict(),
            "itens": itens_dict,
            "bruto": bruto,
            "desconto": pedido.desconto_percentual,
            "liquido": liquido,
        }


