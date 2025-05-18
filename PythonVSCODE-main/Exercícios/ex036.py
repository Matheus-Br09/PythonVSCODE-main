val_casa = float(input('Valor da casa: '))
salario_pessoa = float(input('Seu salário: '))
anos_pagar = int(input('Vai pagar em quantos anos? '))

mes_valor = val_casa / (anos_pagar * 12)
thirty_percent = salario_pessoa * (30/100)

print(f'Para pagar uma casa de R${val_casa:.2f} em {anos_pagar} anos a prestação será de R${mes_valor:.2f}')
if mes_valor > thirty_percent:
    print('Empréstimo NEGADO')
else:
    print('Empréstimo PODE SER CONCEDIDO')

