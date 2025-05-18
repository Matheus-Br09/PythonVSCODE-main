from datetime import date

data_atual = date.today().year
ano_nascimento = int(input("Ano de nascimento: "))
categoria_atleta = data_atual - ano_nascimento
if categoria_atleta <= 9:
    print('Classificação: MIRIM')
elif categoria_atleta <= 14:
    print('Classificação: INFANTIL')
elif categoria_atleta <= 19:
    print("Classificação: JUNIOR")
elif categoria_atleta <= 20:
    print("Classificação: SÊNIOR")
elif categoria_atleta > 21:
    print("Classificação: MASTER")
