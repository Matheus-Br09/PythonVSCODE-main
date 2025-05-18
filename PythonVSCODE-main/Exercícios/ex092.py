from datetime import date

ano_Atual = date.today().year
cadastro_trabalhador = dict()

cadastro_trabalhador['Nome'] = str(input('Nome: ')).strip()
cadastro_trabalhador['Idade'] = int(input('Ano de nascimento: '))
cadastro_trabalhador['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro_trabalhador['CTPS'] != 0:
    cadastro_trabalhador['contratação'] = int(input('Ano de contratação: '))
    cadastro_trabalhador['Salário'] = float(input('Salário: R$'))
    cadastro_trabalhador['Aposentadoria'] = (cadastro_trabalhador['contratação'] + 35) - cadastro_trabalhador['Idade']
cadastro_trabalhador['Idade'] = ano_Atual - cadastro_trabalhador['Idade']

print('=-=-'*10)
for k, v in cadastro_trabalhador.items():
    print(f'{k} tem o valor {v}')


