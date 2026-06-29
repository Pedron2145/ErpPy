from db import db


class Estoque:
    def __init__(self, id_produto, nome_produto, fornecedor, posicao_estoque, quantidade):

        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.fornecedor = fornecedor
        self.posicao_estoque = posicao_estoque
        self.quantidade = quantidade

#verificar
class Busca_produtos:
    def busca_produtos_ID(self, id_produto):

        comando_busca = "SELECT * FROM estoque WHERE id_produto = %s"
        valores_busca = (id_produto,)
        return db.execute_query(comando_busca, valores_busca) 



