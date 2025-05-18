lado1 = float(input('Lado 1: '))
lado2 = float(input('Lado 2: '))
lado3 = float(input('Lado 3: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:
    print('Pode formar um triângulo: ', end='')
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO')
    elif lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado3 == lado1 != lado2:
        print('ISÓSCELES')
    elif lado1 != lado2 != lado3:
        print('ESCALENO')
else:
    print('NÃO pode formar um triângulo')