def listar_todos_clientes(dicionario_clientes: dict):
    for cliente in dicionario_clientes.keys():
        cpf = cliente
        nome = dicionario_clientes[cliente][0]
        data_de_nascimento = dicionario_clientes[cliente][1]
        sexo = dicionario_clientes[cliente][2]
        salario = dicionario_clientes[cliente][3]
        emails = dicionario_clientes[cliente][4]
        telefones = dicionario_clientes[cliente][5]

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


def listar_um_cliente(dicionario_clientes: dict):
    cpf = str(input('Digite o cpf do cliente que gostaria de procurar: ')).strip()
    dados_cliente = dicionario_clientes.get(cpf)

    if not dados_cliente:
        print('Cliente não encontrado. Tente novamente.')
    else:
        nome = dados_cliente[0]
        data_de_nascimento = dados_cliente[1]
        sexo = dados_cliente[2]
        salario = dados_cliente[3]
        emails = dados_cliente[4]
        telefones = dados_cliente[5]

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

def incluir_um_cliente(dicionario_clientes: dict):
    cpf = str(input('Digite o cpf do cliente que gostaria de inserir: '))

    ja_esta_cadastrado = dicionario_clientes.get(cpf)

    while ja_esta_cadastrado:
        print('CPF já cadastrado. Tente novamente.')
        cpf = str(input('Digite o cpf do cliente que gostaria de inserir: '))
        ja_esta_cadastrado = dicionario_clientes.get(cpf)
    
    # TODO validar informações
    nome = str(input('Nome: ')).strip().title()
    data_de_nascimento = str(input('Data de nascimento [dd/mm/aaaa]: ')).strip()
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    salario = float(input('Salário: '))
    emails = []
    telefones = []

    print('--' * 25)

    email = str(input('Email [Pressione ENTER para parar a inserção]: '))
    while email != "":
        emails.append(email)
        email = str(input('Email [Pressione ENTER para parar a inserção]: '))
    
    print('--' * 25)
    
    telefone = str(input('Telefone [Pressione ENTER para parar a inserção]: '))
    while telefone != "":
        telefones.append(telefone)
        telefone = str(input('Telefone [Pressione ENTER para parar a inserção]: '))

    print('--' * 25)
    
    dicionario_clientes[cpf] = [nome, data_de_nascimento, sexo, salario, emails, telefones]

    print('Cliente adicionado com sucesso!')
    print('--' * 25)

def alterar_um_cliente(dicionario_clientes: dict):
    cpf = str(input('Digite o cpf do cliente que deseja alterar: ')).strip()

    dados_cliente = dicionario_clientes.get(cpf)

    while not dados_cliente:
        print('CPF não encontrado. Tente novamente.')
        cpf = str(input('Digite o cpf do cliente que deseja alterar: ')).strip()
        dados_cliente = dicionario_clientes.get(cpf)
    
    nome = dados_cliente[0]
    data_de_nascimento = dados_cliente[1]
    sexo = dados_cliente[2]
    salario = dados_cliente[3]
    emails = dados_cliente[4]
    telefones = dados_cliente[5]

    print('--' * 25)

    print(f'Cliente: {nome}')
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

    # TODO validar informações
    novo_nome = str(input('Digite o novo nome do cliente [Pressione ENTER para não alterar]: '))

    if novo_nome == '':
        novo_nome = nome
    
    nova_data_de_nascimento = str(input('Digite a nova data de nascimento do cliente [Pressione ENTER para não alterar]: '))

    if nova_data_de_nascimento == '':
        nova_data_de_nascimento = data_de_nascimento

    novo_sexo = str(input('Digite o novo sexo do cliente [M/F] [Pressione ENTER para não alterar]: '))

    if novo_sexo == '':
        novo_sexo = sexo
    
    novo_salario = str(input('Digite o novo salário do cliente [Pressione ENTER para não alterar]: '))

    if novo_salario == '':
        novo_salario = salario
    else:
        novo_salario = float(salario)
    
    for i in range(len(emails)):
        quer_alterar = str(input(f'Você deseja alterar o email "{emails[i]}"? [S/N]: '))
        if quer_alterar == 'S':
            email = str(input('Digite o novo email: '))
            emails[i] = email
    
    for i in range(len(telefones)):
        quer_alterar = str(input(f'Você deseja alterar o telefone "{telefones[i]}"? [S/N]: ')).upper().strip()
        if quer_alterar == 'S':
            telefone = str(input('Digite o novo telefone: '))
            telefones[i] = telefone

    cliente_atualizado = [nome, data_de_nascimento, sexo, salario, emails, telefones]
    dicionario_clientes[cpf] = cliente_atualizado
    
    print('Dados do cliente alterados com sucesso!')
    print('--' * 25)

def excluir_um_cliente(dicionario_clientes: dict):
    cpf = str(input('Digite o cpf do cliente que quer excluir: ')).strip()
    dados_cliente = dicionario_clientes.get(cpf)

    while not dados_cliente:
        print('CPF não encontrado. Tente novamente.')
        cpf = str(input('Digite o cpf do cliente que deseja excluir: ')).strip()
        dados_cliente = dicionario_clientes.get(cpf)

    nome = dados_cliente[0]
    
    confirmacao = str(input(f'Você tem certeza que deseja excluir o registro do cliente {nome}? [S/N]: ')).strip().upper()

    if confirmacao == 'S':
        del dicionario_clientes[cpf]

        print(f'Cliente {nome} excluído com sucesso!')
    else:
        print('Operação cancelada.')
    print('--' * 25)