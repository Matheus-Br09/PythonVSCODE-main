from datetime import date

ano_atual = date.today().year
cont = 0

for c in range(1, 5):
    nasc_pessoa = int(input(f'Ano do nascimento {c}° Pessoa: '))
    if ano_atual - nasc_pessoa < 18:
        cont += 1
print(f'Temos {cont} pessoas menores de idade')
