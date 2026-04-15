num = 0
s = 0
for n in range(0, 5):
    num = int(input(f'Informe o número {n+1}: '))
    s += num
print(f'Soma: {s}')
print(f'Média: {s/5}')