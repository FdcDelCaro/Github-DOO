from typing import Any


class Confecçao():

    def __init__(self, nome, tipo, caract, qtd, valor):
        self.nome = nome
        self.tipo = tipo
        self.caract = caract
        self.qtd = qtd
        self.valor = valor

    def seta(self,nome, tipo, caract, qtd, valor) -> None:
        self.nome = nome
        self.tipo = tipo
        self.caract = caract
        self.qtd = qtd
        self.valor = valor

    def getNome(self) -> Any:
        return self.nome
    def getTipo(self) -> Any:
        return self.tipo
      


