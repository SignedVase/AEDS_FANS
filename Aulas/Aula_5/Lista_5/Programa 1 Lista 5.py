nalunos = int(input('Qual a quantidade de alunos? '))
turma = []
rp = []
for i in range(nalunos):
    lista = []
    et1 = 100
    et2 = 100
    et3 = 100
    al = str(input('Informe o nome do aluno: '))
    lista.append(al)
    while et1 > 25:
        et1 = int(input('Informe a nota do aluno na 1° Etapa (max 25): '))
    lista.append(et1)
    while et2 > 30:
        et2 = int(input('Informe a nota do aluno na 2° Etapa (max 30): '))
    lista.append(et2)
    while et3 > 45:
        et3 = int(input('Informe a nota do aluno na 3° Etapa (max 45): '))
    lista.append(et3)
    total = et1 + et2 + et3
    lista.append(total)
    turma.append(lista)
for p in turma:
    if p[4] < 60:
        rp.append(p)
    print(p)
print('Alunos Reprovados')
for r in rp:
    print(r)