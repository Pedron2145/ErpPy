class venda:
    def __init__(self, id_cliente, data, id_produto, quantidade, preco_unitario, total_venda):
        self.id_cliente = id_cliente
        self.data = data
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.total_venda = total_venda

        def calc_total(self):
            self.total_venda = self.quantidade * self.preco_unitario
            return self.total_venda

        