class Curso:
    def __init__(self, codigo, nome, tipo):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo

    def atualizar(self, novo_nome=None, novo_tipo=None):
        if novo_nome:
            self.nome = novo_nome
        if novo_tipo:
            self.tipo = novo_tipo

    def __str__(self):
        return f"{self.codigo} - {self.nome} ({self.tipo})"
