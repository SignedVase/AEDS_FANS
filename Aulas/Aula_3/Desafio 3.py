nome = ''
idade = 200
salario = 0
sexo = ''
estcivil = ''
while len(nome) < 3:
    print('Seu nome deve ter mais que 3 letras')
    nome = input('Digite seu nome: ')
while idade >= 150 or idade <= 0:
    print('A idade deve ser um numero entre 0 e 150')
    idade = int(input('Digite sua idade: '))
while salario <= 0:
    print('Seu salario deve ser maior que 0')
    salario = int(input('Digite seu salario: '))
while sexo != 'M' and sexo != 'F':
    print('Seu sexo deve ser M ou F')
    sexo = str(input('Digite seu sexo: ')).upper()
while estcivil not in ['s','c','d','v']:
    print('Seu estado civil deve ser S para Solteiro, D para Divorciado, C para Casado ou V para Viuvo')
    estcivil = str(input('Digite seu estado civil: ')).lower()