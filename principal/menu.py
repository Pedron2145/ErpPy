"""Menu principal do sistema de controle empresarial via terminal."""

from time import sleep
from db import db
from cadastro import Cliente, vendedor_padrao
from client import CriacaoCliente, EnvioDb
from venda import Venda
from stock import Estoque, Busca_produtos

print('Bem vindo ao meu projeto de Controle \nempresarial via terminal')

'''Garante que a tabela de clientes existe antes de iniciar o menu'''
CriacaoCliente()

'''Valor do loop que será alterado quando o user escolher a opção de sair do programa'''
valor_loop = 1

while valor_loop == 1:
    print('Digite o número da opção desejada: \n1 - Vendas \n2 - Financeiro '
          '\n3 - Estoque \n4 - Relatórios \n5 - Busca\n6 - Sair')

    opcao = int(input('Opção: '))

    '''Estrutura de decisão para cada uma das opções fornecidas no menu principal'''
    if opcao == 1:
        print('Você escolheu a opção Vendas')
        print('Escolha uma opção: \n1 - Cadastrar cliente \n2 - Realizar venda \n3 - Voltar ao menu principal')
        opcao_vendas = int(input('Opção: '))

        if opcao_vendas == 1:
            '''Cadastro de Cliente'''
            print('Você escolheu a opção Cadastrar cliente')
            nome = input('Digite o nome do cliente: ')
            cpf_cnpj = input('Digite o CPF/CNPJ do cliente: ')
            empresa = input('Digite o nome da empresa: ')
            telefone = input('Digite o telefone do cliente: ')
            email = input('Digite o email do cliente: ')
            endereco = input('Digite o endereço do cliente: ')
            status = input('Digite o status do cliente (ativo/inativo): ')

            '''Validação para garantir o preenchimento de todos os campos'''
            if '' in (nome, cpf_cnpj, empresa, telefone, email, endereco, status):
                print('Todos os campos devem ser preenchidos. Por favor, tente novamente.')
            elif status not in ('ativo', 'inativo'):
                print('Status inválido. Use "ativo" ou "inativo".')
            else:
                '''Criação do objeto cliente e envio para o banco de dados'''
                cliente = Cliente(nome, cpf_cnpj, empresa, telefone, email, endereco, status)
                envio = EnvioDb(cliente)
                envio.enviar_para_db()

            sleep(2)

        elif opcao_vendas == 2:
            '''Realizar venda'''
            print('Você escolheu a opção Realizar venda')
            print('Digite seu ID de vendedor e sua senha')

            '''Autenticação do vendedor para registro e rastreio da venda'''
            id_vendedor = input('Digite seu ID de vendedor: ')
            senha = input('Digite sua senha: ')

            if id_vendedor == '' or senha == '':
                print('Todos os campos devem ser preenchidos. Por favor, tente novamente.')
            elif int(id_vendedor) != vendedor_padrao.id_vendedor or senha != vendedor_padrao.senha:
                print('ID de vendedor ou senha incorretos. Por favor, tente novamente.')
            else:
                '''Realização da venda, já que o vendedor foi autenticado'''
                id_cliente = input('Digite o ID do cliente: ')
                data = input('Digite a data da venda: ')
                id_produto = input('Digite o ID do produto: ')
                quantidade = input('Digite a quantidade vendida: ')
                preco_unitario = input('Digite o preço unitário do produto: ')

                '''Validação para garantir o preenchimento de todos os campos'''
                if '' in (id_cliente, data, id_produto, quantidade, preco_unitario):
                    print('Todos os campos devem ser preenchidos. Por favor, tente novamente.')
                else:
                    quantidade = int(quantidade)
                    preco_unitario = float(preco_unitario)
                    venda = Venda(id_cliente, data, id_produto, quantidade, preco_unitario)
                    total = venda.calc_total()
                    print('Venda realizada com sucesso! Total da venda: R${:.2f}'.format(total))

            sleep(2)

        elif opcao_vendas == 3:
            print('Voltando ao menu principal...')
            sleep(2)

        else:
            print('Opção inválida. Por favor, tente novamente.')

    elif opcao == 2:
        print('Você escolheu a opção Financeiro')
        sleep(2)

    elif opcao == 3:
        print('Você escolheu a opção Estoque')
        print('Escolha uma opção \n1 - Consulta\n2 - Entrada\n3 - Ajuste\n 4 - Cadastro\n 5 - Saída')
        opcao_estoque = int(input(': '))
        if (opcao_estoque == 1):
            print('Consulta')
            id_produto = int(input('Digite o código do produto a ser consultado\n: '))

            if id_produto == '':
                print('você deve digitar um valor')
            else: #verificar
                busca = Busca_produtos(id_produto)
                busca.busca_produtos_id()
                
                print('Código: {}\nProduto: {}\nFornecedor: {}\nPosição: {}\n Quantidade: {}'.format(Estoque.id_produto, Estoque.nome_produto, Estoque.fornecedor, Estoque.posicao_estoque, Estoque.quantidade))



        elif (opcao_estoque == 2):
            print('Entrada')    
        sleep(2)

    elif opcao == 4:
        print('Você escolheu a opção Relatórios')
        sleep(2)

    elif opcao == 5:
        print('Você escolheu a opção Busca')
        sleep(2)

    elif opcao == 6:
        print('Saindo do programa...')
        valor_loop = 0

    else:
        print('Opção inválida. Por favor, tente novamente.')

db.close_connection()
