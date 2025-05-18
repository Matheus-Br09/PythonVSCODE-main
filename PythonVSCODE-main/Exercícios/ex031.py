print('''PROMOÇÃO DE VIAGEM, viagem acima de 200km pagam R$0,45 por KM''')
price_passagem = float(input('Digite a distÂncia da viagem[Km]: '))
valor_viagem = price_passagem * 0.50
if price_passagem > 200:
    valor_viagem = price_passagem * 0.45
    print(f'Você vai pagar o valor de R${valor_viagem:.2f}'. replace('.', ','))
else:
    print(f'Você vai pagar o valor de R${valor_viagem:.2f}'.replace('.', ','))