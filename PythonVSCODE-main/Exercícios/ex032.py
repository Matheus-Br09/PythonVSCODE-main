from datetime import date

valor_ano = int(input("Digite o ano: "))
if valor_ano == 0:
    valor_ano = date.today().year
if valor_ano % 4 == 0 and valor_ano % 100 != 0 or valor_ano % 400 == 0:
    print(f'{valor_ano} É bissexto')
else:
    print(f'{valor_ano} NÃO É bissexto')
