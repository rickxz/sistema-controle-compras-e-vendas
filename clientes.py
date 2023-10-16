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

    