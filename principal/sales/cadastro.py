"""Classes de dados para clientes e vendedores."""


class Cliente:
    def __init__(self, nome, cpf_cnpj, empresa, telefone, email, endereco, status):
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.empresa = empresa
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.status = status


class Vendedor:
    def __init__(self, id_vendedor, senha):
        self.id_vendedor = id_vendedor
        self.senha = senha


'''Vendedor de exemplo para autenticação no menu'''
vendedor_padrao = Vendedor(1234, 'senha123')
