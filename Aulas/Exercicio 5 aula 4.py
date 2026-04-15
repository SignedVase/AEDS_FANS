frase = str(input('Digite uma frase: ')).strip().upper()
pal = 0
junto = frase.replace(' ', '')
for c in range(len(junto)):
    if junto[c] == junto[len(junto) -1- c]:
        pal += 1
if pal == len(junto):
    print('A frase é um Palindromo')
else:
    print('A frase não é um palindromo')