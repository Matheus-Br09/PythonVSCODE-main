from datetime import date

ano_atual = date.today().year
dados_trabalhador = dict()

dados_trabalhador["Nome"] = str(input("Nome: "))
age = int(input("Ano de nascimento: "))
dados_trabalhador["Idade"] = ano_atual - age
dados_trabalhador["CTPS"] = int(input("Carteira de trabalho: "))

if dados_trabalhador["CTPS"] != 0:
    dados_trabalhador["Contratação"] = int(input("Ano de contratação: "))
    dados_trabalhador["Salário"] = float(input("Salário: R$"))
    dados_trabalhador["Aposentadoria"] = (dados_trabalhador["Contratação"] - age) + 35
print("-=-="*15)
for k, v in dados_trabalhador.items():
        print(f'{k} tem o valor {v}')
print('-=-='*15)