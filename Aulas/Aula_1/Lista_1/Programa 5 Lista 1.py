turno = ''
saud = ''
while turno != 'M' or turno != 'V' or turno != 'N':
    turno = str(input('Qual turno você estuda? ')).strip()[0].upper()
    if turno == 'M':
        saud = 'Bom Dia!'
        break
    elif turno == 'V':
        saud = 'Boa Tarde!'
        break
    elif turno == 'N':
        saud = 'Boa Noite!'
        break
    else:
        saud = 'Valor Inválido!'
    print(saud)
print(saud)
