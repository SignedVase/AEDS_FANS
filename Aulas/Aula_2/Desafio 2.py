dia = 0
Semana = ['Domingo','Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado']
while 1 > dia or dia > 7:
    try:
        dia = int(input('Informe o dia (1-7): '))
    except ValueError:
        print('Informe um número!')
    if 1 <= dia <= 7:
        print(Semana[dia-1])
        break
    else:
        print('Dia Inválido')