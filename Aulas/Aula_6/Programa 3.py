n = int(input('Informe o tamanho do dicionario: '))
quad = {}
for i in range(1, n + 1):
    quad.update({i: i * i})
print(quad)