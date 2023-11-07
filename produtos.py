def listar_todos_produtos(dicionario_produtos: dict):
    for produto in dicionario_produtos.keys():
        descricao = dicionario_produtos[produto][0]
        peso = dicionario_produtos[produto][1]
        preco = dicionario_produtos[produto][2]
        desconto = dicionario_produtos[produto][3]
        validade = dicionario_produtos[produto][4]
        print (f'{descricao},{peso},{preco},{desconto},{validade}')

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
        print (f'{descricao},{peso},{preco},{desconto},{validade}')

      
def incluir_um_produto(dicionario_produtos: dict):
    produto = str(input('Digite o produto que gostaria de inserir: '))

    ja_esta_cadastrado = dicionario_produtos.get(produto)

    while ja_esta_cadastrado:
        print('Produto já cadastrado. Tente novamente.')
        codigo = str(input('Digite o codigo do produto que gostaria de inserir: '))
        ja_esta_cadastrado = dicionario_produtos.get(codigo)
    # TODO validar informações
    descricao = str(input('Produto: ')).strip().title()
    peso = float(input('Peso do produto:  '))
    preco = float(input('Preco do produto: '))
    desconto = float(input('Desconto do produto: '))
    validade = str(input('Validade do produto: '))

    print('--' * 25)

    


        
