qnt = int(input('Informe a quantidade de pessoas: '))
s = 0
for c in range(0, qnt):
    n = int(input(f'Informe a idade da pessoa {c+1}: '))
    s += n
med = s/qnt
print(f'Média: {med}')
if med < 26:
    print('A turma é Jovem (Média de 0 à 25 anos)')
elif med > 60:
    print('A turma é Idosa (Média maior que 60 anos)')
else:
    print('A turma é Adulta (Média entre 26 e 60 anos)')