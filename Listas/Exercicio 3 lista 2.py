sali = float(input('Digite seu salario para saber seu aumeto: '))
salf = 0
if 1200 >= sali:
    salf = sali * 1.2
elif 1200 < sali <= 1800:
    salf = sali * 1.15
elif 1800 < sali <= 2500:
    salf = sali * 1.1
elif sali > 2500:
    salf = sali * 1.05
print(round(salf, 2))