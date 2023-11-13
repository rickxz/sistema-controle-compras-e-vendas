from datetime import date

def validar_cpf(cpf: str):
    if len(cpf) != 14:
        return False

    if not cpf[0:3].isnumeric() or not cpf[4:7].isnumeric() or not cpf[8:11].isnumeric() or not cpf[12:14].isnumeric():
        return False

    if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        return False

    return True

def validar_nome(nome: str):
    return len(nome) > 0 and nome.replace(' ', '').isalpha()

def validar_data(data: str, pode_ser_no_futuro: bool = False):
    if len(data) != 10:
        return False

    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])

    dias_por_mes = {
        1: 31, 
        2: 29 if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0) else 28, 
        3: 31, 
        4: 30, 
        5: 31, 
        6: 30, 
        7: 31, 
        8: 31, 
        9: 30, 
        10: 31, 
        11: 30,
        12: 31
    }

    if dia < 1 or dia > dias_por_mes.get(mes, 31):
        return False
    if mes < 1 or mes > 12:
        return False
    if ano < 1900:
        return False
    
    hoje = date.today()

    if not pode_ser_no_futuro:
        if ano > hoje.year:
            return False

        if mes > hoje.month and ano == hoje.year:
            return False

        if dia > hoje.day and mes == hoje.month and ano == hoje.year:
            return False

    return True

def validar_sexo(sexo: str):
    return sexo == 'M' or sexo == 'F'

def validar_valor(valor: float):
    return valor >= 0

def validar_hora(hora: int):
    return hora >= 0 and hora <= 23

def atualizar_arquivo_clientes(dicionario_clientes: dict):
    with open('clientes.txt', 'w', encoding='utf-8') as arquivo_clientes:
        for cpf, dados_cliente in dicionario_clientes.items():
            nome = dados_cliente[0]
            data_de_nascimento = dados_cliente[1]
            sexo = dados_cliente[2]
            salario = dados_cliente[3]
            emails = dados_cliente[4]
            telefones = dados_cliente[5]

            arquivo_clientes.write(f'{cpf}|{nome}|{data_de_nascimento}|{sexo}|{salario}|{",".join(emails)}|{",".join(telefones)}\n')

def atualizar_arquivo_produtos(dicionario_produtos: dict):
    with open('produtos.txt', 'w', encoding='utf-8') as arquivo_produtos:
        for codigo, dados_produto in dicionario_produtos.items():
            descricao = dados_produto[0]
            peso = dados_produto[1]
            preco = dados_produto[2]
            desconto = dados_produto[3]
            validade = dados_produto[4]

            arquivo_produtos.write(f'{codigo}|{descricao}|{peso}|{preco}|{desconto}|{validade}\n')

def atualizar_arquivo_compras_vendas(dicionario_compra_venda: dict):
    with open('compras_vendas.txt', 'w', encoding='utf-8') as arquivo_compra_venda:
        for dados_compra, valor in dicionario_compra_venda.items():
            cpf_cliente = dados_compra[0]
            codigo_produto = dados_compra[1]
            data = dados_compra[2]
            hora = dados_compra[3]

            arquivo_compra_venda.write(f'{cpf_cliente}|{codigo_produto}|{data}|{hora}|{valor}\n')