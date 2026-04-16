qnt = int(input('Informe a quantidade de turmas: '))
val = 0
for turm in range(0, qnt):
    num = int(input(f'Informe a quantidade de alunos da turma {turm + 1}: '))
    val += num
print(f'A média de alunos é: {val/qnt}')