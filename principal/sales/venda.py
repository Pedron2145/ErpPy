"""Classe de venda e cálculo do total."""

import uuid


class Venda:
    def __init__(self, id_cliente, data, id_produto, quantidade, preco_unitario, total_venda=0):
        self.id = uuid.uuid4()
        self.id_cliente = id_cliente
        self.data = data
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.total_venda = total_venda

    def calc_total(self):
        """Calcula o total da venda (quantidade x preço unitário)."""
        self.total_venda = self.quantidade * self.preco_unitario
        return self.total_venda
