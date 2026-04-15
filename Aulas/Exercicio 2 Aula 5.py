l = []
val = 0
for c in range(1, 5):
    n = int(input(f'Infome a nota {c}: '))
    l.append(n)
    val += n
print(l)
print(val/4)