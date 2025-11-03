class Produto:
    def __init__(self, id, nome, preco, etiquetas=None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.etiquetas = etiquetas or []
        self.ativo = True

    def aplicar_desconto(self, percentual):
        return self.preco * (1 - percentual)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "preco_formatado": f"R$ {self.preco:,.2f}",
            "etiquetas": ",".join(self.etiquetas),
        }


