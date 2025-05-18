nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2
if media < 5:
    print('REPROVADO')
elif media >= 5 and media < 6.9:
    print("RECUPERAÇÃO")
elif media > 7 and media <= 10:
    print("APROVADO")
else:
    print("DIGITE VALORES VÁLIDOS")
