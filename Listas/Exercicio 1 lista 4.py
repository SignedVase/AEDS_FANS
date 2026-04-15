nome = str(input('Informe o nome: ')).upper()
for l in range(len(nome)-1, -1, -1):
    print(nome[l], end='')