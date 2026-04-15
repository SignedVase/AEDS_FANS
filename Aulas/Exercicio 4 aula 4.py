num = int(input('Digite um número de 1 à 99: '))
ind = ["um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
dec = ["vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
dez = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
if len(str(num)) == 1:
    print(ind[int(num)-1])
elif 10 <= num <= 19:
    print(dez[int(num)-10])
elif num > 19 and str(num)[1] == '0':
    print(dec[int(str(num)[0])-2])
elif num > 19 and str(num)[1] != '0':
    print(f'{dec[int(str(num)[0])-2]} e {ind[int(str(num)[1])-1]}')