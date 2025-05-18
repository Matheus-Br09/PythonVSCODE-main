cont = 0
num = int(input("Digite o valor: "))
for c in range(1, num+1):
    if num % c == 0 and num % 1 == 0:
        cont += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(c, end='\033[m ')
print()
print(f'O número {num} foi divivísvel {cont} vezes')
print('E por isso ele ', end='')
if cont == 2:
    print("É PRIMO!")
else:
    print('NÃO É PRIMO!')