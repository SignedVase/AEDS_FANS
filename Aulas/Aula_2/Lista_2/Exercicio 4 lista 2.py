n1 = float(input('Informe o primeiro numero: '))
n2 = float(input('Informe o segundo numero: '))
print('Operações:\n + soma\n - subtração\n / divisão\n * multiplicação')
op = str(input('Informe a operação que deseja realizar: '))
resu = float
if op == '+':
    resu = n1 + n2
elif op == '-':
    resu = n1 - n2
elif op == '/':
    resu = n1 / n2
elif op == '*':
    resu = n1 * n2
else:
    print('Operação Inválida!')
print(f'Resultado: {round(resu, 2)}')
poi = ''
if resu // 2 == 1:
    poi = 'par'
else:
    poi = 'impar'
pon = ''
if resu >= 0:
    pon = 'positivo'
else:
    pon = 'negativo'
iod = ''
if resu - round(resu) == 0:
    iod = 'inteiro'
else:
    iod = 'decimal'
print(f'Numero {poi}\nNumero {pon}\nNumero {iod}')