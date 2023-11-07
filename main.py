from clientes import alterar_um_cliente, incluir_um_cliente, listar_todos_clientes, listar_um_cliente
from produtos import listar_todos_produtos
from produtos import listar_um_produto,incluir_um_produto

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

dicionario_produtos = {'1':
                       ['creme',
                        15,
                        0.50,
                        0,
                        '19/2025'
                        ]}

def submenu_produtos():
    print('1. Listar todos os produtos')
    print('2. Listar um produto')
    print('3. Incluir um produto')
    print('4. Alterar um produto')
    print('5. Excluir um produto')

    opcao_submenu_produtos= int(input('Digite uma opção: '))
    if opcao_submenu_produtos == 1:
        listar_todos_produtos(dicionario_produtos)
    elif opcao_submenu_produtos == 2:
        listar_um_produto(dicionario_produtos)
    elif opcao_submenu_produtos == 3:
        incluir_um_produto(dicionario_produtos)
            


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

    
main()