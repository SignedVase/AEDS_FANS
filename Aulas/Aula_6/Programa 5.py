molde = {'marca' : '',
         'modelo' : '',
         'ano' : 0,
         'quilometragem' : 0,
         'preco_venda' : 0}
carros = []
n = int(input('Quantidade de carros: '))
for c in range(n):
    molde['marca'] = input('Marca: ')
    molde['modelo'] = input('Modelo: ')
    molde['ano'] = int(input('Ano: '))
    molde['quilometragem'] = int(input('KM: '))
    molde['preco_venda'] =  int(input('Preço Venda: '))
    carros.append(molde.copy())
print(carros)