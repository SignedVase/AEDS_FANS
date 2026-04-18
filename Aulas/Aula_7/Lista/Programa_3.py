def soma(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

op = 0
while op != 1 and op != 2 and op != 3 and op != 4:
    print('---Bem vindo a Calculadora---\n'
          'Qual opção você deseja?\n'
          '1 - Soma\n'
          '2 - Subtração\n'
          '3 - Multiplicação\n'
          '4 - Divisão')
    op = int(input('Opção: '))
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if op == 1:
    result = soma(n1, n2)
    oper = 'Soma'
elif op == 2:
    result = sub(n1, n2)
    oper = 'Subtração'
elif op == 3:
    result = mult(n1, n2)
    oper = 'Multiplicação'
elif op == 4:
    result = div(n1, n2)
    oper = 'Divisão'
print(f'O Resultado da {oper} é {result}')