from math import sqrt

print('--->>', "Fórmulha de Bhaskara", '<<---')

valor_a = int(input("Digite o valor de A: "))
valor_b = int(input("Digite o valor de B: "))
valor_c = int(input("Digite o valor de C: "))

def bhaskara(a, b, c):
    delta = (b ** 2) - 4 * a * c
    if a == 0:
        print('VALOR DE A IGUAL ZERO, >> ERRO <<')
    if delta < 0:
        print("DELTA NEGATIVO, >> ERRO <<")
    else:
        x1 = (-b + sqrt(delta)) / 2 * a
        x2 = (-b - sqrt(delta)) / 2 * a
        if x1 > 0 and x2 > 0:
            print(f'Os valores de X1 e X2 respectivamente são: ({x1:.2f}), ({x2:.2f})')
        elif x2 > 0:
            print(f'O valor de Bhaskara de x2: {x2:.2f}')
        elif x1 > 0: 
            print(f'O valor de Bhaskara de x1: {x1:.2f}')


bhaskara(valor_a, valor_b, valor_c)