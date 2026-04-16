tel = str(input('Informe o numero de telefone: '))
tel2 = ''
cont = 0
if '-' in tel:
    if len(tel) == 9:
        tel = '9' + tel
else:
    for n in tel:
        cont += 1
        tel2 += n
        if len(tel) == 9:
            if cont == 5:
                tel2 += '-'
        elif len(tel) == 8:
            if cont == 1:
                tel2 = '9' + tel2
            elif cont == 4:
                tel2 += '-'
    tel = tel2
print(tel)