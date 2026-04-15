letra = '234'
while len(letra) > 1 and letra.isalnum() == True:
    letra = str(input('Digite uma letra: ')).strip().lower()
    if len(letra) == 1:
        break
    print('Digite apenas uma letra!')

if letra in 'aeiou':
    print('É uma vogal')
else:
    print('É uma consoante')