val_salario = float(input("Digite seu sálario: "))
aumento_salario = 0
if val_salario > 1250:
    aumento_salario =  val_salario + (val_salario * (10/100))
    print('Você ganhou um aumento de 10% !!!')
if val_salario < 1250:
    aumento_salario = val_salario + (val_salario * (15/100))
    print('Você ganhou um aumento de 15% !!!')
print(f'Você vai passar a ganhar R${aumento_salario: .2f}'.replace('.', ','))
