from random import randint

computador = jogador = cont = 0
par_impar = ''
print('=-=-'*6)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=-'*6)
while True:
    jogador = int(input('Digite sua jogada: '))
    computador = randint(0, 10)

    while True:
        par_impar = str(input("Par ou ímpar? [P/I] ")).upper().strip()[0]
        if par_impar in 'PI':
            break
        else:
            print('DIGITE UM VALOR CORRETO!!')
    
    print('=-=-'*15)

    print(f'Você jogou {jogador} e o computador {computador}. ', end='')
    print(f'Total de {jogador + computador} ', end='')

    if (jogador + computador) % 2 == 0:
        print("DEU PAR")
        if par_impar == 'P':
            print("\033[34mVOCÊ VENCEU!!!\033[m")
            print("Vamos jogar novamente...")
            cont += 1
        else:
            print("\033[31mVOCÊ PERDEU!!!\033[m")
            break
    elif (jogador + computador) % 2 == 1:
        print('DEU ÍMPAR')
        if par_impar == 'I':
            print("\033[34mVOCÊ VENCEU!!!\033[m")
            print("Vamos jogar novamente...")
            cont += 1
        else:
            print("\033[31mVOCÊ PERDEU!!!\033[m")
            break

    print('=-=-'*15)

print("=-=-"*15)
print(f"Você ganhou {cont} partida(s)!!!")
print('=-=-'*15)