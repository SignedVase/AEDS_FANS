def listaSet(lista):
    sete = set()
    for c in lista:
        print(c)
        sete.add(c)
    return sete

preLista = str(input('Digite os valores (separador com ","): '))
lista = preLista.split(',')
lista.sort()
print(lista)
ltest = []
sete = listaSet(lista)
print(sete)
for num in sete:
    ltest.append(num)
ltest.sort()
print(ltest)
if lista == ltest:
    print('True')
else:
    print('False')