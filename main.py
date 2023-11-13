from clientes import alterar_um_cliente, excluir_um_cliente, incluir_um_cliente, listar_todos_clientes, listar_um_cliente
from produtos import listar_todos_produtos, listar_um_produto, incluir_um_produto, alterar_um_produto, excluir_produto
from compras_vendas import alterar_uma_compra_venda, excluir_uma_compra_venda, incluir_uma_compra_venda, listar_todas_compras_vendas, listar_uma_compra_venda
from relatorios import relatorio_clientes, relatorio_compras_e_vendas, relatorio_produtos

def mostra_menu_principal():
    print('1. Submenu de clientes')
    print('2. Submenu de produtos')
    print('3. Submenu de compra/venda')
    print('4. Submenu de relatórios')
    print('5. Sair')
    

def mostra_submenu_clientes():
    print('1. Listar todos os clientes')
    print('2. Listar um cliente')
    print('3. Incluir um cliente')
    print('4. Alterar um cliente')
    print('5. Excluir um cliente')

    opcao_submenu_clientes = int(input('Digite uma opção: '))

    while opcao_submenu_clientes < 1 or opcao_submenu_clientes > 5:
        print('Opção inválida. Tente novamente.')
        opcao_submenu_clientes = int(input('Digite uma opção: '))

    print('--' * 25)
    
    if opcao_submenu_clientes == 1:
        listar_todos_clientes(dicionario_clientes)
    
    elif opcao_submenu_clientes == 2:
        listar_um_cliente(dicionario_clientes)
    
    elif opcao_submenu_clientes == 3:
        incluir_um_cliente(dicionario_clientes)

    elif opcao_submenu_clientes == 4:
        alterar_um_cliente(dicionario_clientes)
    
    elif opcao_submenu_clientes == 5:
        excluir_um_cliente(dicionario_clientes)


def submenu_produtos():
    print('1. Listar todos os produtos')
    print('2. Listar um produto')
    print('3. Incluir um produto')
    print('4. Alterar um produto')
    print('5. Excluir um produto')

    opcao_submenu_produtos= int(input('Digite uma opção: '))

    while opcao_submenu_produtos < 1 or opcao_submenu_produtos > 5:
        print('Opção inválida. Tente novamente.')
        opcao_submenu_produtos = int(input('Digite uma opção: '))

    print('--' * 25)

    if opcao_submenu_produtos == 1:
        listar_todos_produtos(dicionario_produtos)
    elif opcao_submenu_produtos == 2:
        listar_um_produto(dicionario_produtos)
    elif opcao_submenu_produtos == 3:
        incluir_um_produto(dicionario_produtos)
    elif opcao_submenu_produtos == 4:
        alterar_um_produto(dicionario_produtos) 
    elif opcao_submenu_produtos == 5:
        excluir_produto(dicionario_produtos)    


def mostra_submenu_compra_venda():
    print('1. Listar todos as compras/vendas')
    print('2. Listar uma compra/venda')
    print('3. Incluir uma compra/venda')
    print('4. Alterar uma compra/venda')
    print('5. Excluir uma compra/venda')

    opcao_submenu_compra_venda = int(input('Digite uma opção: '))

    while opcao_submenu_compra_venda < 1 or opcao_submenu_compra_venda > 5:
        print('Opção inválida. Tente novamente.')
        opcao_submenu_compra_venda = int(input('Digite uma opção: '))

    print('--' * 25)
    
    if opcao_submenu_compra_venda == 1:
        listar_todas_compras_vendas(dicionario_compra_venda)
    
    elif opcao_submenu_compra_venda == 2:
        listar_uma_compra_venda(dicionario_compra_venda)
    
    elif opcao_submenu_compra_venda == 3:
        incluir_uma_compra_venda(dicionario_clientes, dicionario_produtos, dicionario_compra_venda)

    elif opcao_submenu_compra_venda == 4:
        alterar_uma_compra_venda(dicionario_compra_venda)

    elif opcao_submenu_compra_venda == 5:
        excluir_uma_compra_venda(dicionario_compra_venda)


def mostra_submenu_relatorios():
    print('1. Listar os clientes que possuem mais do que X telefones.')
    print('2. Listar os produtos que já tiveram sua data de validade vencida.')
    print('3. Listar compras/vendas em um determinado intervalo de tempo.')

    opcao_submenu_relatorios = int(input('Digite uma opção: '))

    while opcao_submenu_relatorios < 1 or opcao_submenu_relatorios > 3:
        print('Opção inválida. Tente novamente.')
        opcao_submenu_relatorios = int(input('Digite uma opção: '))
    
    print('--' * 25)

    if opcao_submenu_relatorios == 1:
        relatorio_clientes(dicionario_clientes)
    elif opcao_submenu_relatorios == 2:
        relatorio_produtos(dicionario_produtos)
    else:
        relatorio_compras_e_vendas(dicionario_clientes, dicionario_produtos, dicionario_compra_venda)


with open('clientes.txt', 'r', encoding='utf-8') as arquivo_clientes:
    dicionario_clientes = {}
    for linha in arquivo_clientes:
        cpf, nome, data_nascimento, sexo, salario, emails, telefones = linha.strip().split('|')
        dicionario_clientes[cpf] = [nome, data_nascimento, sexo, float(salario), emails.split(','), telefones.split(',')]

with open('produtos.txt', 'r', encoding='utf-8') as arquivo_produtos:
    dicionario_produtos = {}
    for linha in arquivo_produtos:
        codigo, descricao, peso, preco, desconto, validade = linha.strip().split('|')
        dicionario_produtos[codigo] = [descricao, float(peso), float(preco), float(desconto), validade]

with open('compras_vendas.txt', 'r', encoding='utf-8') as arquivo_compra_venda:
    dicionario_compra_venda = {}
    for linha in arquivo_compra_venda:
        cpf, codigo, data, hora, valor = linha.strip().split('|')
        dicionario_compra_venda[(cpf, codigo, data, int(hora))] = float(valor)

def main():
    opcao = 0
    while opcao != 5:
        mostra_menu_principal()
        opcao = int(input('Digite uma opção: '))
        while opcao < 1 or opcao > 5:
            print('Opção inválida. Tente novamente.')
            opcao = int(input('Digite uma opção: '))

        print('--' * 25)

        if opcao == 1:
            mostra_submenu_clientes()
        elif opcao == 2:
            submenu_produtos()
        elif opcao == 3:
            mostra_submenu_compra_venda()
        elif opcao == 4:
            mostra_submenu_relatorios()

    
main()