quad = 0
while  1 > quad or quad > 20:
    quad = int(input('Digite o tamanho do quadrado (valor entre 1 e 20): '))
for c in range(quad):
    print('*'*quad)