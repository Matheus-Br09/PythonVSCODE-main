from random import randint

print('==='*10, 'Jogo do Acerto', '==='*10)

computador = randint(0, 10)
jogador = 0
tentativas = 0

print('Pensei em um número... tente acertar qual entre 0 e 10!!!')

while jogador != computador:
    jogador = int(input("Palpite: "))
    tentativas += 1
    if 0 <= jogador <= 10:
        if computador < jogador:
            print(f'Tente um valor menor...')
        elif computador > jogador:
            print('Tente um valor maior...')
    else:
        print('\033[31mDIGITE UM VALOR VÁLIDO!!!\033[m')
    

if tentativas == 1:
    print('DE PRIMEIRA, parabéns!!!')
else:
    print(f'Você deu {tentativas} palpites antes de acertar!')
