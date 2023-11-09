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

def validar_data(data: str):
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
    
    data_usuario = f'{dia}/{mes}/{ano}'
    hoje = date.today().strftime('%d/%m/%Y')

    if data_usuario > hoje:
        return False

    return True

def validar_sexo(sexo: str):
    return sexo == 'M' or sexo == 'F'

def validar_valor(salario: float):
    return salario < 0

def validar_hora(hora: int):
    return hora >= 0 and hora <= 23