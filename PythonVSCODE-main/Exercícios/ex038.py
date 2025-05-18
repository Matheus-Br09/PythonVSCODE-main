num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
if num1 > num2:
    print(f'O primeiro valor: {num1} é MAIOR')
elif num2 > num1:
    print(f'O segundo valor: {num2} é MAIOR')
else:
    print('Os dois valores são IGUAIS')