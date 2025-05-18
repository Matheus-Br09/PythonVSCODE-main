price_product = float(input('Preço do produto: R$'))

print('''FORMA DE PAGAMENTO
[1] Dinheiro/Cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais''')
type_OfPayment = int(input('Escolha: '))

desconto = 0
parcelas = 0

if type_OfPayment == 1:
    desconto = price_product - (price_product * (10/100))
    print(f'Você ganhou um desconto de 10%!!!')
    print(f'O valor do produto ficou por R${desconto:.2f}')
if type_OfPayment == 2:
    desconto = price_product - (price_product * (5/100))
    print('Você ganhou um desconto de 5%!!!')
    print(f'O valor do produto ficou por R%{desconto:.2f}')
if type_OfPayment == 3:
    parcelas = price_product / 2
    print(f'Parcelado em 2x, você pagará R${parcelas:.2f} por mês')
if type_OfPayment == 4:
    desconto = price_product + (price_product * (20/100))
    qtd_parcelas = int(input('Quantas parcelas? '))
    juros_parcela = (price_product + (price_product * (20/100))) / qtd_parcelas
    print(f'Sua compra será parcelada em {qtd_parcelas}x de R${juros_parcela:.2f} COM JUROS.')
    print(f'Sua compra de R${price_product:.2f} vai custar R${desconto:.2f} no final.')
else:
    print('DIGITE UM VALOR VÁLIDO!!!')
