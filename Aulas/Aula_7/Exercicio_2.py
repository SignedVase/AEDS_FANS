def datacao(dat, ext=False):
    dat = dat.split('-')
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    if ext:
        print(f'{dat[0]} de {meses[int(dat[1])-1]} de {dat[2]}')
    else:
        print(f'{dat[0]}/{dat[1]}/{dat[2]}')

datacao('12-01-2026')
datacao('12-01-2026', True)