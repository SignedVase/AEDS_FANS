n1 = -1
n2 = -1
while n1 < 0 or n1 > 10:
    n1 = float(input('Digite sua primeira nota: '))
    if n1 < 0 or n1 > 10:
        print('Digite uma nota válida!')
while n2 < 0 or n2 > 10:
    n2 = float(input('Digite sua segunda nota: '))
    if n2 < 0 or n2 > 10:
        print('Digite uma nota válida!')
med = (n1+n2)/2
if med == 10:
    print('Aprovado com Distinção')
elif med >= 7:
    print(f'Aprovado com média {med}')
else:
    print('Reprovado')
