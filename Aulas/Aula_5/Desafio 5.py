from random import choice
from time import sleep

def VencerH(li1):
    for a in range(3):
        if li1[a][0] == li1[a][1] == li1[a][2] and li1[a][0] != ' ' and li1[a][1] != ' ' and li1[a][2]!= ' ':
            return True
    return False
def VencerV(li1):
     for i in range(3):
        if li1[0][i] == li1[1][i] == li1[2][i] and li1[0][i] != ' ' and li1[1][i] != ' ' and li1[2][i] != ' ':
            return True
     return False
def VencerTrans1(li1):
    if li1[0][0] == li1[1][1] == li1[2][2] and li1[0][0] != ' ' and li1[1][1] != ' ' and li1[2][2] != ' ':
        return True
    else:
        return False
def VencerTrans2(li1):
    if li1[0][2] == li1[1][1] == li1[2][0] and li1[0][2] != ' ' and li1[1][1] != ' ' and li1[2][0] != ' ':
        return True
    else:
        return False
def Bot(li1):
    for w in range(3):
        for j in range(3):
            if li1[w][j] == ' ':
                vaz.append((w,j))
    linha, coluna = choice(vaz)
    return linha, coluna

li1 = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
venc = ''
opa = False
opb = False
opc = False
opd = False
while not (opa or opb or opc or opd) and (' ' in li1[0] or ' ' in li1[1] or ' ' in li1[2]):
    vaz = []
    for tab in li1:
        print(tab)
    l = int(input('Informe a linha onde deseja posicionar: ')) - 1
    c = int(input('Informe a coluna onde deseja posicionar: ')) - 1
    if li1[l][c] in ' ':
        li1[l][c] = 'X'
    else:
        print('Linha inválida')
        continue
    if VencerV(li1):
        venc = 'Ganhou'
        break
    if VencerH(li1):
        venc = 'Ganhou'
        break
    if VencerTrans1(li1):
        venc = 'Ganhou'
        break
    if VencerTrans2(li1):
        venc = 'Ganhou'
        break
    lin, col = Bot(li1)
    li1[lin][col] = 'O'
    opa = VencerH(li1)
    opb = VencerV(li1)
    opc = VencerTrans1(li1)
    opd = VencerTrans2(li1)
    if opa or opb or opc or opd:
        venc = 'Perdeu'
    else:
        venc = 'Empatou'
for tab in li1:
    print(tab)
print(f'Você {venc}!')
sleep(1)