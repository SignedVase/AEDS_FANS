montantei = float(input('Qual o montante sera investido? R$'))
tax = str(input('Qual o Rendimento Mensal? '))
temp = int(input('Por quantos meses? '))
for nm in tax:
    if nm != '%':
        taxa = int(nm)/100
rend1 = 1 + taxa
rendf = rend1 ** temp
montantef = montantei * rendf
print(round(montantef, 2))
