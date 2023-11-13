from datetime import datetime

from utils import validar_data

def relatorio_clientes(dicionario_clientes: dict):
    quantia_telefones = int(input('Digite a quantia de telefones mínima para listagem: '))

    contagem_clientes = 0

    for cliente in dicionario_clientes.keys():
        telefones = dicionario_clientes[cliente][5]
        if len(telefones) > quantia_telefones:
            contagem_clientes += 1
            cpf = cliente
            nome = dicionario_clientes[cliente][0]
            data_de_nascimento = dicionario_clientes[cliente][1]
            sexo = dicionario_clientes[cliente][2]
            salario = dicionario_clientes[cliente][3]
            emails = dicionario_clientes[cliente][4]

            print(f'Cliente: {nome}')
            print(f'CPF: {cpf}')
            print(f'Data de nascimento: {data_de_nascimento}')
            print(f'Sexo: {sexo}')
            print(f'Salário: R${salario:.2f}')
            print('Emails: ', end='')
            for email in emails:
                print(email, end=' ')
            print('\nTelefones: ', end='')
            for telefone in telefones: 
                print(telefone, end=' ')

            print()
            print('--' * 25)

    if contagem_clientes == 0:
        print(f'Nenhum cliente possui mais de {quantia_telefones} telefones.')

def relatorio_produtos(dicionario_produtos: dict):
    hoje = datetime.today()

    print('Produtos que já tiveram a data de validade vencida: ')
    for produto in dicionario_produtos.keys():
        data_validade = dicionario_produtos[produto][4]
        if datetime.strptime(data_validade, '%d/%m/%Y') < hoje:
            descricao = dicionario_produtos[produto][0]
            peso = dicionario_produtos[produto][1]
            preco = dicionario_produtos[produto][2]
            desconto = dicionario_produtos[produto][3]
            
            print(f'Código do produto: {produto}')
            print(f'Descrição: {descricao}')
            print(f'Peso: {peso}kg')
            print(f'Preço: R${preco:.2f}')
            print(f'Desconto: R${desconto:.2f}')
            print(f'Data de validade: {data_validade}')
            print('--' * 25)


def relatorio_compras_e_vendas(dicionario_clientes: dict, dicionario_produtos: dict, dicionario_compra_venda: dict):
    data_inicio = str(input('Digite a data de início (dd/mm/aaaa): '))

    while not validar_data(data_inicio):
        print('Data inválida. Tente novamente.')
        data_inicio = str(input('Digite a data de início (dd/mm/aaaa): '))

    data_fim = str(input('Digite a data de fim (dd/mm/aaaa): '))

    while not validar_data(data_fim, pode_ser_no_futuro=True):
        print('Data inválida. Tente novamente.')
        data_fim = str(input('Digite a data de fim (dd/mm/aaaa): '))

    data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y')
    data_fim = datetime.strptime(data_fim, '%d/%m/%Y')

    for compra_venda in dicionario_compra_venda.keys():
        data_compra_venda = compra_venda[2]
        if data_inicio <= datetime.strptime(data_compra_venda, '%d/%m/%Y') and data_fim >= datetime.strptime(data_compra_venda, '%d/%m/%Y'):
            cpf_cliente = compra_venda[0]
            nome_cliente = dicionario_clientes[cpf_cliente][0]
            codigo_produto = compra_venda[1]
            descricao_produto = dicionario_produtos[codigo_produto][0]
            hora = compra_venda[3]
            valor = dicionario_compra_venda[compra_venda]

            print('--' * 25)
            print(f'Cliente: {nome_cliente}')
            print(f'Produto: {descricao_produto}')
            print(f'Valor: R${valor:.2f}')
            print(f'Data: {data_compra_venda}')
            print(f'Hora: {hora}h')
            
