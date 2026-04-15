turma = {}
moldeAluno = {'nome' : '',
              'et1' : 0,
              'et2' : 0,
              'et3' : 0,
              'total' : 0}
n = int(input('Quantidade de alunos: '))
for c in range(n):
    matri = str(input('Matricula: '))
    moldeAluno['nome'] = input('Nome: ')
    moldeAluno['et1'] = int(input('Nota Etapa 1: '))
    moldeAluno['et2'] = int(input('Nota Etapa 2: '))
    moldeAluno['et3'] = int(input('Nota Etapa 3: '))
    moldeAluno['total'] =  moldeAluno['et3'] + moldeAluno['et2'] + moldeAluno['et1']
    turma.update({matri: moldeAluno.copy()})
for al in turma:
    print(al, end=', ')
    print(turma[al])