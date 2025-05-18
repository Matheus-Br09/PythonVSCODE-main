from datetime import date

ano_nasc = int(input('Ano de nascimento: '))
data = date.today().year

print(f'Quem nasceu em {ano_nasc} tem {data-ano_nasc} ano(s) em {data}.')
if data - ano_nasc == 18:
    print('VOCÊ PRECISA SE ALISTAR IMEDIATAMENTE!!!')
elif data-ano_nasc < 18:
    saldo = 18 - (data - ano_nasc)
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    print(f'Seu alistamnto será em {data + saldo}.')
elif data-ano_nasc > 18:
    saldo = (data - ano_nasc) - 18
    print(f'Você deveria ter se alistado há {(saldo)} ano(s)')
    print(f'Você se alistou em {data - saldo}.')