def par(n):
    if n % 2 == 0:
        return 'Par'
    else:
        return 'Impar'

num = int(input('Digite um numero: '))
print(f'O número é {par(num)}')