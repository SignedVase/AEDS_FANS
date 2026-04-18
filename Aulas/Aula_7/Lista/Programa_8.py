from random import randint
from time import sleep

def jogada():
    n1 = randint(1,6)
    n2 = randint(1,6)
    return n1 + n2

c = 0
while True:
    if c <= 1:
        c += 1
    jogo = jogada()
    print(jogo)
    sleep(1)
    if c == 1:
        if jogo == 7 or jogo == 11:
            print('Parabens, você tirou Natural, você Ganhou!')
            break
        elif jogo == 2 or jogo == 3 or jogo == 12:
            print('Parabens, você tirou Craps, você Perdeu!')
            break
        else:
            ponto = jogo
    else:
        if jogo == ponto:
            print('Parabens! Você venceu!')
            break
        elif jogo == 7:
            print('Você perdeu!')
            break