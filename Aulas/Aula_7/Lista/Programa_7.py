def valorPrest(val,at):
    if at != 0:
        multa = val * 3 / 100
        jur = val * at / 1000
        ad = multa + jur
    else:
        ad = 0
    valf = val + ad
    return valf

valor = 1
relDia = []
while valor > 0:
    valor = float(input('Informe o valor da parcela (0 para encerrar): '))
    if valor == 0:
        break
    atraso = int(input('Informe quantos dias de atraso no pagamento: '))
    valor = valorPrest(valor,atraso)
    relDia.append(valor)
    print(f'O valor a ser pago é de {valor}')
print('Relatório de valores pagos no dia de hoje: ')
for val in relDia:
    print(val)