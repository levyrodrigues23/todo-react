class Cliente:
    def __init__(self, id, nome, email, tags=[]):
        self.id = id
        self.nome = nome
        self.email = email
        self.tags = tags
        self.ativo = True

    def email_valido(self) -> bool:
        return "@" in self.email

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "email_exibicao": f"{self.nome} <{self.email}>",
            "tags": ",".join(sorted(set(self.tags))) if self.tags else "",
        }

    def _normalizar_nome(self):
        self.nome = (self.nome or "").strip().title()


