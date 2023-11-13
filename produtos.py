from utils import atualizar_arquivo_produtos, validar_data, validar_valor


def listar_todos_produtos(dicionario_produtos: dict):
    for produto in dicionario_produtos.keys():
        descricao = dicionario_produtos[produto][0]
        peso = dicionario_produtos[produto][1]
        preco = dicionario_produtos[produto][2]
        desconto = dicionario_produtos[produto][3]
        validade = dicionario_produtos[produto][4]
        
        print(f'Código: {produto}')
        print(f'Produto: {descricao}')
        print(f'Peso: {peso}kg')
        print(f'Preço: R${preco:.2f}')
        print(f'Desconto: R${desconto:.2f}')
        print(f'Validade: {validade}')
        print('--' * 25)

def listar_um_produto(dicionario_produtos: dict):
    codigo = str(input('Digite o codigo do produto que gostaria de procurar: ')).strip()
    dados_produto = dicionario_produtos.get(codigo)

    if not dados_produto:
        print('Produto não encontrado. Tente novamente.')
    else:
        descricao = dicionario_produtos[codigo][0]
        peso = dicionario_produtos[codigo][1]
        preco = dicionario_produtos[codigo][2]
        desconto = dicionario_produtos[codigo][3]
        validade = dicionario_produtos[codigo][4]

        print(f'Código: {codigo}')
        print(f'Produto: {descricao}')
        print(f'Peso: {peso}kg')
        print(f'Preço: R${preco:.2f}')
        print(f'Desconto: R${desconto:.2f}')
        print(f'Validade: {validade}')

def incluir_um_produto(dicionario_produtos: dict):
    codigo = str(input('Digite o código do produto que gostaria de inserir: '))

    ja_esta_cadastrado = dicionario_produtos.get(codigo)

    while ja_esta_cadastrado:
        print('Produto já cadastrado. Tente novamente.')
        codigo = str(input('Digite o codigo do produto que gostaria de inserir: '))
        ja_esta_cadastrado = dicionario_produtos.get(codigo)

    descricao = str(input('Produto: ')).strip().title()
    peso = float(input('Peso do produto em kg:  '))

    while not validar_valor(peso):
        print('Peso inválido. Tente novamente.')
        peso = float(input('Peso do produto em kg:  '))

    preco = float(input('Preco  [Pressione ENTER para não alterar] '))

    while not validar_valor(preco):
        print('Preço inválido. Tente novamente.')
        preco = float(input('Preco do produto: '))

    desconto = float(input('Desconto do produto: '))
    while not validar_valor(desconto):
        print('Desconto inválido. Tente novamente.')
        desconto = float(input('Desconto do produto: '))

    validade = str(input('Validade do produto: '))

    while not validar_data(validade, pode_ser_no_futuro=True):
        print('Data inválida. Tente novamente.')
        validade = str(input('Validade do produto: '))

    dicionario_produtos[codigo] = [descricao, peso, preco, desconto, validade]
    atualizar_arquivo_produtos(dicionario_produtos)

    print('Produto cadastrado com sucesso!')
    print('--' * 25)

def alterar_um_produto(dicionario_produtos: dict):
    codigo = str(input('Digite o código do produto que deseja alterar: ')).strip()

    dados_produto = dicionario_produtos.get(codigo)

    while not dados_produto:
        print('Código não encontrado. Tente novamente.')
        codigo = str(input('Digite o código do produto que deseja alterar: ')).strip()
        dados_produto = dicionario_produtos.get(codigo)
    
    descricao = dados_produto[0]
    peso = dados_produto[1]
    preco = dados_produto[2]
    desconto = dados_produto[3]
    validade = dados_produto[4]

    print('--' * 25)

    print(f'Produto: {descricao}')
    print(f'Peso: {peso}kg')
    print(f'Preço: R${preco:.2f}')
    print(f'Desconto R${desconto:.2f}')
    print(f'Validade: {validade}')

    print('--' * 25)

    nova_descricao = str(input('Digite a nova descrição do produto [Pressione ENTER para não alterar]: ')).strip().title()

    if nova_descricao == '':
        nova_descricao = descricao

    novo_peso = str(input('Digite o novo peso do produto [Pressione ENTER para não alterar]: ')).strip()

    if novo_peso == '':
        novo_peso = peso
    else:
        while not validar_valor(float(novo_peso)):
            print('Peso inválido. Tente novamente.')
            novo_peso = str(input('Digite o novo peso do produto [Pressione ENTER para não alterar]: '))
            novo_peso = float(novo_peso)

    novo_preco = str(input('Digite o novo preço do produto [Pressione ENTER para não alterar]: ')).strip()
    if novo_preco == '':
        novo_preco = preco
    else:
        while not validar_valor(float(novo_preco)):
            print('Preço inválido. Tente novamente.')
            novo_preco = str(input('Digite o novo preço do produto [Pressione ENTER para não alterar]: '))
            novo_preco = float(novo_preco)
    

    novo_desconto = str(input('Digite o novo desconto do produto [Pressione ENTER para não alterar]: ')).strip()
    if novo_desconto == '':
        novo_desconto = desconto
    else:
        while not validar_valor(float(novo_desconto)):
            print('Desconto inválido. Tente novamente.')
            novo_desconto = str(input('Digite o novo desconto do produto [Pressione ENTER para não alterar]: '))
            novo_desconto = float(novo_desconto)
    
    nova_data_de_validade = str(input('Digite a nova data de validade do produto [Pressione ENTER para não alterar]: ')).strip()
    if nova_data_de_validade == '':
        nova_data_de_validade = validade
    else:
        while not validar_data(nova_data_de_validade, pode_ser_no_futuro=True):
            print('Data inválida. Tente novamente.')
            nova_data_de_validade = str(input('Digite a nova data de validade do produto [Pressione ENTER para não alterar]: ')).strip()

    dicionario_produtos[codigo] = [nova_descricao, novo_peso, novo_preco, novo_desconto, nova_data_de_validade]
    atualizar_arquivo_produtos(dicionario_produtos)

    print('--' * 25)
    print('Produto alterado com sucesso!')


def excluir_produto(dicionario_produtos: dict):
    codigo = str(input('Digite o código do produto que deseja excluir: ')).strip()

    dados_produto = dicionario_produtos.get(codigo)

    while not dados_produto:
        print('Código não encontrado. Tente novamente.')
        codigo = str(input('Digite o código do produto que deseja excluir: ')).strip()
        dados_produto = dicionario_produtos.get(codigo)

    produto = dados_produto[0]
    
    confirmacao = str(input(f'Você tem certeza que deseja excluir o produto {produto}? [S/N]: ')).strip().upper()

    while not confirmacao in 'SN':
        print('Opção inválida. Tente novamente.')
        confirmacao = str(input(f'Você tem certeza que deseja excluir o produto {produto}? [S/N]: ')).strip().upper()

    if confirmacao == 'S':
        del dicionario_produtos[codigo]
        print(f'Produto {produto} excluído com sucesso!')

        atualizar_arquivo_produtos(dicionario_produtos)
    else:
        print('Operação cancelada.')
    print('--' * 25) 