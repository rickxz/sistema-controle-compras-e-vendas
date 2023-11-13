from utils import atualizar_arquivo_compras_vendas, validar_cpf, validar_data, validar_hora, validar_valor


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
        print(f'Hora da compra/venda {hora}h')
        print(f'Valor da compra: R$ {valor:.2f}')
        print('--' * 25)

def listar_uma_compra_venda(dicionario_compra_venda: dict):
    cpf_cliente = str(input('Digite o CPF do cliente da compra/venda que deseja listar [xxx.xxx.xxx-xx]: ')).strip()
    
    while not validar_cpf(cpf_cliente):
        print('CPF inválido. Tente novamente.')
        cpf_cliente = str(input('Digite o CPF do cliente da compra/venda que deseja listar [xxx.xxx.xxx-xx]: ')).strip()
        

    codigo_produto = str(input('Digite o código do produto da compra/venda que deseja listar: ')).strip().upper()
    data = str(input('Digite a data da compra/venda que deseja listar: ')).strip()

    while not validar_data(data):
        print('Data inválida. Tente novamente.')
        data = str(input('Digite a data da compra/venda que deseja listar: ')).strip()

    hora = int(input('Digite a hora da compra/venda que deseja listar: '))

    while not validar_hora(hora):
        print('Hora inválida. Tente novamente.')
        hora = int(input('Digite a hora da compra/venda que deseja listar: '))

    chave_dicionario = (cpf_cliente, codigo_produto, data, hora)

    dados_compra_venda = dicionario_compra_venda.get(chave_dicionario)
    if not dados_compra_venda:
        print('Dados da compra e venda não encontrados.')
    else:
        print('--' * 25)
        valor = dicionario_compra_venda[chave_dicionario]
        print(f'CPF do cliente: {cpf_cliente}')
        print(f'Código do produto: {codigo_produto}')
        print(f'Data da compra/venda: {data}')
        print(f'Hora da compra/venda {hora}h')
        print(f'Valor da compra: R$ {valor:.2f}')

    print('--' * 25)

def incluir_uma_compra_venda(dicionario_clientes: dict, dicionario_produtos: dict, dicionario_compra_venda: dict):
    cpf_cliente = str(input('Digite o CPF do cliente [xxx.xxx.xxx-xx]: ')).strip()

    while not validar_cpf(cpf_cliente):
        print('CPF inválido. Tente novamente.')
        cpf_cliente = str(input('Digite o CPF do cliente [xxx.xxx.xxx-xx]: ')).strip()

    while not dicionario_clientes.get(cpf_cliente):
        print('CPF não encontrado. Tente novamente.')
        cpf_cliente = str(input('Digite o CPF do cliente [xxx.xxx.xxx-xx]: ')).strip()

    codigo_produto = str(input('Digite o código do produto: ')).strip().upper()

    while not dicionario_produtos.get(codigo_produto):
        print('Código do produto não encontrado. Tente novamente.')
        codigo_produto = str(input('Digite o código do produto: ')).strip().upper()

    data = str(input('Digite a data da compra/venda: ')).strip()

    while not validar_data(data):
        print('Data inválida. Tente novamente.')
        data = str(input('Digite a data da compra/venda: ')).strip()

    hora = int(input('Digite a hora da compra/venda: '))

    while not validar_hora(hora):
        print('Hora inválida. Tente novamente.')
        hora = int(input('Digite a hora da compra/venda: '))

    valor = float(input('Digite o valor da compra/venda: '))

    while not validar_valor(valor):
        print('Valor inválido. Tente novamente.')
        valor = float(input('Digite o valor da compra/venda: '))

    chave_dicionario = (cpf_cliente, codigo_produto, data, hora)

    dicionario_compra_venda[chave_dicionario] = valor
    atualizar_arquivo_compras_vendas(dicionario_compra_venda)

    print('Compra/venda inserida com sucesso!')
    print('--' * 25)

def alterar_uma_compra_venda(dicionario_compra_venda: dict):
    cpf_cliente = str(input('Digite o CPF do cliente da compra/venda que deseja alterar [xxx.xxx.xxx-xx]: ')).strip()

    while not validar_cpf(cpf_cliente):
        print('CPF inválido. Tente novamente.')
        cpf_cliente = str(input('Digite o CPF do cliente da compra/venda que deseja alterar [xxx.xxx.xxx-xx]: ')).strip()
    
    codigo_produto = str(input('Digite o código do produto da compra/venda que deseja alterar: ')).strip().upper()
    data = str(input('Digite a data da compra/venda que deseja alterar: ')).strip()

    while not validar_data(data):
        print('Data inválida. Tente novamente.')
        data = str(input('Digite a data da compra/venda que deseja alterar: ')).strip()

    hora = int(input('Digite a hora da compra/venda que deseja alterar: '))

    while not validar_hora(hora):
        print('Hora inválida. Tente novamente.')
        hora = int(input('Digite a hora da compra/venda que deseja alterar: '))

    chave_dicionario = (cpf_cliente, codigo_produto, data, hora)

    dados_compra_venda = dicionario_compra_venda.get(chave_dicionario)
    if not dados_compra_venda:
        print('Dados da compra e venda não encontrados.')
    else:
        valor = dicionario_compra_venda[chave_dicionario]
        novo_valor = float(input(f'Digite o novo valor da compra [Valor atual: R$ {valor:.2f}]: '))

        while not validar_valor(novo_valor):
            print('Valor inválido. Tente novamente.')
            novo_valor = float(input(f'Digite o novo valor da compra [Valor atual: R$ {valor:.2f}]: '))

        dicionario_compra_venda[chave_dicionario] = novo_valor
        atualizar_arquivo_compras_vendas(dicionario_compra_venda)
        
        print('Compra/venda alterada com sucesso!')

    print('--' * 25)

def excluir_uma_compra_venda(dicionario_compra_venda: dict):
    cpf_cliente = str(input('Digite o CPF do cliente da compra/venda que deseja excluir [xxx.xxx.xxx-xx]: ')).strip()

    while not validar_cpf(cpf_cliente):
        print('CPF inválido. Tente novamente.')
        cpf_cliente = str(input('Digite o CPF do cliente da compra/venda que deseja excluir [xxx.xxx.xxx-xx]: ')).strip()

    codigo_produto = str(input('Digite o código do produto da compra/venda que deseja excluir: ')).strip().upper()
    data = str(input('Digite a data da compra/venda que deseja excluir: ')).strip()

    while not validar_data(data):
        print('Data inválida. Tente novamente.')
        data = str(input('Digite a data da compra/venda que deseja excluir: ')).strip()

    hora = int(input('Digite a hora da compra/venda que deseja excluir: '))

    while not validar_hora(hora):
        print('Hora inválida. Tente novamente.')
        hora = int(input('Digite a hora da compra/venda que deseja excluir: '))

    chave_dicionario = (cpf_cliente, codigo_produto, data, hora)

    dados_compra_venda = dicionario_compra_venda.get(chave_dicionario)
    if not dados_compra_venda:
        print('Dados da compra e venda não encontrados.')
    else:
        confirmacao = str(input(f'Você tem certeza que deseja excluir esse registro? [S/N]: ')).strip().upper()

        if confirmacao == 'S':
            del dicionario_compra_venda[chave_dicionario]
            print('Compra/venda excluída com sucesso!')
            atualizar_arquivo_compras_vendas(dicionario_compra_venda)
        else:
            print('Operação cancelada.')
    
    print('--' * 25)
