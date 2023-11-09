from compras_vendas import alterar_uma_compra_venda, excluir_uma_compra_venda, incluir_uma_compra_venda, listar_todas_compras_vendas, listar_uma_compra_venda
from clientes import alterar_um_cliente, excluir_um_cliente, incluir_um_cliente, listar_todos_clientes, listar_um_cliente
from relatorios import relatorio_clientes


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
        incluir_uma_compra_venda(dicionario_compra_venda)

    elif opcao_submenu_compra_venda == 4:
        alterar_uma_compra_venda(dicionario_compra_venda)

    elif opcao_submenu_compra_venda == 5:
        excluir_uma_compra_venda(dicionario_compra_venda)


dicionario_clientes = {'1': 
                       ['José', 
                        '06/12/2021', 
                        'M', 
                        1280, 
                        ['jose@gmail.com', 'jose@hotmail.com'],
                        ['16980234151', '1691723810']
                        ],
                        '2': [
                            'Maria',
                            '01/03/2004',
                            'F',
                            1325,
                            ['maria@gmail.com', 'maria@hotmail.com'],
                            ['16192748', '161868129']
                        ]
                    }

dicionario_compra_venda = {
    ('1', '1', '06/11/2023', 23): 30,
    ('2', '2', '05/11/2023', 24): 31,
}

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
            pass
        elif opcao == 3:
            mostra_submenu_compra_venda()
        elif opcao == 4:
            mostra_submenu_relatorios()

    
main()