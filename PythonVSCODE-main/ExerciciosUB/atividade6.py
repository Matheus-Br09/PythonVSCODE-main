valor_produto = int(input('Digite o valor do produto: R$'))
total_pago = int(input("Preço pago: R$"))
troco = total_pago - valor_produto
ced = 50
totced = 0
while True:
    if troco < 0:
        print("Valor insuficiente para a compra")
        break
    else:
        if troco >= ced:
            troco -= ced
            totced += 1
        else:
            if totced > 0:
                print(f'Total de {totced} cédulas de R${ced}')
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            totced = 0
            if troco == 0:
                break


        