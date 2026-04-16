def media(*numeros):
    sm = 0
    for n in numeros:
        sm += int(n)
    med = sm / len(numeros)
    return med
print(media(3,3,6))