op = 1
EstoquePr = 0
EstoqueMP = 0
while op != 0:
    print('=== SISTEMA DE CONTROLE ===')
    print('1 - Comprar')
    print('2 - Produção')
    print('3 - Venda')
    print('4 - Estoque')
    print('0 - Sair')
    op = int(input('Escolha uma opção: '))
    if op == 1:
        MP = int(input('Informe a quantidade comprada: '))
        EstoqueMP += MP
        print(f'Estoque Matéria Prima: {EstoqueMP}')
    if op == 2:
        Pr = int(input('Informe a quantidade de produtos que deseja fazer: '))
        if Pr * 2 > EstoqueMP:
            print('Materia Prima Insuficiente!')
            continue
        else:
            EstoqueMP -= Pr * 2
            EstoquePr += Pr
            print(f'Estoque Matéria Prima: {EstoqueMP}')
            print(f'Estoque de Produtos: {EstoquePr}')
    if op == 3:
        Vend = int(input('Informe a quantidade de propudos a vender: '))
        if Vend > EstoquePr:
            print('Estoque Insuficiente!')
            continue
        else:
            EstoquePr -= Vend
            print(f'Quantidade de Produtos: {EstoquePr}')
            print(f'Quantidade de Produtos Vendidos: {Vend}')
    if op == 4:
        print(f'Estoque Matéria Prima: {EstoqueMP}')
        print(f'Estoque Produção: {EstoquePr}')