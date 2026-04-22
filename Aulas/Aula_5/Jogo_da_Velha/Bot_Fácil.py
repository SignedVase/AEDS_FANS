from random import choice

def Facil(li1, vaz):
    for w in range(3):
        for j in range(3):
            if li1[w][j] == ' ':
                vaz.append((w,j))
    linha, coluna = choice(vaz)
    return linha, coluna