import re
cpf = str(input('Informe o CPF para validação: '))
val = re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf)
if val:
    print('CPF Válido')
else:
    print('CPF Inválido')