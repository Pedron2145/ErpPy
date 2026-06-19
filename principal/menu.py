('Bem vindo ao meu projeto de Controle \nempresarial via terminal')

from unittest import case
from time import sleep
from sales.cadastro import cadastro_cliente
from sales.venda import venda

valorLoop = 1

while valorLoop == 1:
    print('Digite o número da opção desejada: \n1 - Vendas \n2 - Financeiro \n3 - Estoque \n4 - Relatórios \n5 - Busca\n6 - Sair')

    opcao = int(input('Opção: '))


    if opcao == 1:
        print('Você escolheu a opção Vendas')
        print('Escolha uma opção: \n1 - Cadastrar cliente \n2 - Realizar venda \n3 - Voltar ao menu principal')
        opcao_vendas = int(input('Opção: '))
        if opcao_vendas == 1:
            print('Você escolheu a opção Cadastrar cliente')
            nome = input('Digite o nome do cliente: ')
            cpf_cnpj = input('Digite o CPF/CNPJ do cliente: ')
            empresa = input('Digite o nome da empresa: ')
            telefone = input('Digite o telefone do cliente: ')
            email = input('Digite o email do cliente: ')
            endereco = input('Digite o endereço do cliente: ')
            status = input('Digite o status do cliente: ')

            if (nome == '' or cpf_cnpj == '' or empresa == '' or telefone == '' or email == '' or endereco == '' or status == ''):
                print('Todos os campos devem ser preenchidos. Por favor, tente novamente.')

            else:
                cliente = cadastro_cliente(nome, cpf_cnpj, empresa, telefone, email, endereco, status)
                print('Cliente {} cadastrado com sucesso!'.format(cliente.nome))
            
            sleep(2)
        elif opcao_vendas == 2:
            print('Você escolheu a opção Realizar venda')
            id_cliente = input('Digite o ID do cliente: ')
            data = input('Digite a data da venda: ')
            id_produto = input('Digite o ID do produto: ')
            quantidade = int(input('Digite a quantidade vendida: '))
            preco_unitario = float(input('Digite o preço unitário do produto: '))
            
            if (id_cliente == '' or data == '' or id_produto == '' or quantidade == '' or preco_unitario == ''):
                print('Todos os campos devem ser preenchidos. Por favor, tente novamente.')
            else:
                venda = venda(id_cliente, data, id_produto, quantidade, preco_unitario, 0)
                total = venda.calc_total()
                print('Venda realizada com sucesso! Total da venda: R${:.2f}'.format(total))

            sleep(2)
        elif opcao_vendas == 3:
            print('Voltando ao menu principal...')
            sleep(2)

        sleep(2)

    elif opcao == 2:
        print('Você escolheu a opção Financeiro')
        sleep(2)

    elif opcao == 3:
        print('Você escolheu a opção Estoque')
        sleep(2)

    elif opcao == 4:
        print('Você escolheu a opção Relatórios')
        sleep(2)

    elif opcao == 5:
        print('Você escolheu a opção Busca')
        sleep(2)

    elif opcao == 6:
        print('Saindo do programa...')
        valorLoop = 0

    else:
        print('Opção inválida. Por favor, tente novamente.')





