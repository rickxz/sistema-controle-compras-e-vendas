def listar_todas_compras_vendas(dicionario_compra_venda: dict):
    for compra_venda in dicionario_compra_venda.keys():
        cpf_cliente = compra_venda[0]
        codigo_produto = compra_venda[1]
        data = compra_venda[2]
        hora = compra_venda[3]
        valor = dicionario_compra_venda[compra_venda]


        print(f'CPF do cliente: {cpf_cliente}')
        print(f'Código do produto: {codigo_produto}')
        print(f'Data da compra/venda: {data}')
        print(f'Hora da compra/venda {hora} h')
        print(f'Valor da compra: R$ {valor}')
        print('--' * 25)

def listar_uma_compra_venda(dicionario_compra_venda: dict):
    cpf_cliente = str(input('Digite o CPF do cliente que deseja listar uma compra/venda: '))
    codigo_produto = str(input('Digite o código do produto que deseja listar uma compra/venda: '))
    data = str(input('Digite a data da compra/venda que deseja listar: '))
    hora = str(input('Digite a hora da compra/venda que deseja listar: '))

    chave_dicionario = (cpf_cliente, codigo_produto, data, hora)

    dados_compra_venda = dicionario_compra_venda.get(chave_dicionario)
    if not dados_compra_venda:
        print('Dados da compra e venda não encontrados. Tente novamente.')
    else:
        valor = dicionario_compra_venda[chave_dicionario]
        print(f'CPF do cliente: {cpf_cliente}')
        print(f'Código do produto: {codigo_produto}')
        print(f'Data da compra/venda: {data}')
        print(f'Hora da compra/venda {hora} h')
        print(f'Valor da compra: R$ {valor}')

    print('--' * 25)

def incluir_uma_compra_venda(dicionario_compra_venda: dict):
    # TODO Validar as informações
    
    cpf_cliente = str(input('Digite o CPF do cliente: '))
    codigo_produto = str(input('Digite o código do produto: '))
    data = str(input('Digite a data da compra/venda: '))
    hora = str(input('Digite a hora da compra/venda: '))
    valor = str(input('Digite o valor da compra/venda: '))

    chave_dicionario = (cpf_cliente, codigo_produto, data, hora)

    dicionario_compra_venda[chave_dicionario] = valor

    print('Compra/venda inserida com sucesso!')
    print(dicionario_compra_venda)

