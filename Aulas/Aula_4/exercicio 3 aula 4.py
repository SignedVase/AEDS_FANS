data = str(input('Digite uma data (dd/mm/aaaa): '))
data = data.split('/')
mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
print(f'{data[0]} de {mes[int(data[1]) - 1]} de {data[2]}')