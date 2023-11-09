def relatorio_clientes(dicionario_clientes: dict):
    quantia_telefones = int(input('Digite a quantia de telefones mínima para listagem: '))

    contagem_clientes = 0

    for cliente in dicionario_clientes.keys():
        telefones = dicionario_clientes[cliente][5]
        if len(telefones) > quantia_telefones:
            contagem_clientes += 1
            # TODO refatorar a listagem de clientes em uma função que receba o cpf como parâmetro
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