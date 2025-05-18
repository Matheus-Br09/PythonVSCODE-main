numero = int(input('Digite um valor: '))
cont = 0

for i in range(1, numero+1):
    if numero % i == 0 and numero % 1 == 0:
        cont += 1
        
if cont == 2:
    print(f'{numero} é PRIMO')
else:
    print(f'{numero} NÃO É PRIMO')

