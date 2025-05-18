num_fatorial = int(input('calcule o Fatorial: '))
resultado = 1
cont = num_fatorial
print(f'{num_fatorial}! = ', end='')
while cont > 0:
    print(f'{cont}', end='')
    print(f' x ' if cont > 1 else ' = ', end='')
    resultado *= cont
    cont -= 1
print(f'{resultado}')
    