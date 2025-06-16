valor = int(input("Valor inteiro do produto: "))
pago = int(input("Digite o valor pago: "))
troco = pago - valor
if troco <= 0:
    print(f'Você ainda deve pagar o produto, ou ele está totalmente pago.')
else:
    notas_50 = troco // 50
    troco %= 50

    nota_20 = troco // 20
    troco %= 20

    nota_10 = troco // 10
    troco %= 10

    nota_1 = troco

if notas_50 > 0:
    print(f'Notas de R$50: {int(notas_50)}')
if nota_20 > 0:
    print(f'Notas de R$20: {int(nota_20)}')
if nota_10 > 0:
    print(f'Notas de R$10: {int(nota_10)}')
if nota_1 > 0:
    print(f'Notas de R$1: {int(nota_1)}')