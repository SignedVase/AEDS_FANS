def cadUsuario(nome, idade):
    print(f'Olá {nome}, você tem {idade} anos.')
    with open('Usuários.txt', 'a') as arq:
        arq.write(f'{nome} {idade}\n')
    print('Sucesso')
nm = str(input('Seu nome: '))
idd = int(input('Sua idade: '))
cadUsuario(nm, idd)
