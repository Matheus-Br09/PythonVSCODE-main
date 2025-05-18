numero_fatorial = int(input('Digite o número: '))
fat = 1
print(f'{numero_fatorial}! = {numero_fatorial} ', end='')
for i in range(1 ,numero_fatorial):
    print(f'x {numero_fatorial-i} ', end='')
    fat *= i+1
print(f'= {fat}')
    