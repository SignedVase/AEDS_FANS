frase = str(input('Informe uma frase para ser analisada: ')).lower()
pala = str(input('Informe uma letra especifica da frase: ')).lower()
c = 0
for p in frase:
    if p == pala:
        c += 1
print(f'A quantidade de ocorrencias da letra {pala.upper()} é {c}')