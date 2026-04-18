def novoProduto(mar, mod, num, pr_com, pr_vend, qnt):
    pro = {'marca':mar,
           'modelo':mod,
           'numeração': num,
           'preco_compra': pr_com,
           'preco_venda': pr_vend,
           'quantidade': qnt}
    return pro
def listarProdutos(prod):
    x = prod.items()
    for produc in x:
        print(produc)

produtos = {}
op = 0
cod = 0
while op != 3:
    op = 0
    while op != 1 and op != 2 and op != 3:
        print('Qual operação deseja realizar?\n'
              '1 - Cadastrar novo produto\n'
              '2 - Listar produtos\n'
              '3 - Sair')
        op = int(input('Informe a opção: '))
    if op == 1:
        cod += 1
        ma = str(input('Marca do produto: '))
        mo = str(input('MOdelo do produto: '))
        n = int(input('Numeração do produto: '))
        com = float(input('Preço de Compra do produto: '))
        vend = float(input('Preço de Venda do produto: '))
        quan = int(input('Quantidade do produto: '))
        produtos.update( {cod: novoProduto(ma, mo, n, com, vend, quan)})
    if op == 2:
        listarProdutos(produtos)
    if op == 3:
        break
print('Obrigado, Volte Sempre.')