from time import sleep

continuar = True
primeiro_numero = float(input("1° Valor: "))
segundo_numero = float(input('2° Valor: '))

while continuar == True:
    
    print('''====OPÇÕES====
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do Programa''')
    escolher_opcao = int(input('Sua escolha: '))
    if 1 <= escolher_opcao <= 5:
        if escolher_opcao == 1:
            print('=='*10)
            print(f'{primeiro_numero:.1f} + {segundo_numero:.1f} = {primeiro_numero + segundo_numero:.1f}')
            print('=='*10)
            sleep(1)
        elif escolher_opcao == 2:
            print('=='*10)
            print(f'{primeiro_numero:.2f} x {segundo_numero:.2f} = {primeiro_numero * segundo_numero:.2f}')
            print('=='*10)
            sleep(1)
        elif escolher_opcao == 3:
            print('=='*10)
            if primeiro_numero > segundo_numero:
                print(f'{primeiro_numero} é MAIOR que {segundo_numero}')
            else:
                print(f'{segundo_numero} é MAIOR que {primeiro_numero}')
            print('=='*10)
            sleep(1)
        elif escolher_opcao == 4:
            print('==='*10)
            print('Digite os novos valores: ')
            primeiro_numero = float(input("1° Valor: "))
            segundo_numero = float(input('2° Valor: '))
        elif escolher_opcao == 5:
            continuar = False
print('=='*3,'FIM', '=='*3)
