from random import randint

computador = randint(0,2)
jogadas = 'Pedra', 'Papel', 'Tesoura'
print('''JOGADAS
[1] Pedra
[2] Papel
[3] Tesoura''')
jogador_choice = int(input("Sua jogada: "))
if jogador_choice == 1:
    if computador == 0:
        print(f'Jogador: {jogadas[jogador_choice-1]} x {jogadas[computador]} :Computador')
        print('\033[33mEMPATE\033[m')
    if computador == 1:
        print(f'Jogador: {jogadas[jogador_choice-1]} x {jogadas[computador]} :Computador')
        print('\033[31mDERROTA\033[m')
    if computador == 2:
        print(f'Jogador: {jogadas[jogador_choice-1]} x {jogadas[computador]} :Computador')
        print('\033[34mVITÓRIA\033[m')
if jogador_choice == 2:
    if computador == 0:
        print(f'Jogador: {jogadas[jogador_choice-1]} x {jogadas[computador]} :Computador')
        print('\033[34mVITÓRIA\033[m')
    if computador == 1:
        print(f'Jogador: {jogadas[jogador_choice-1]} x {jogadas[computador]} :Computador')
        print('\033[33mEMPATE\033[m')
    if computador == 2:
        print(f'Jogador: {jogadas[jogador_choice-1]} x {jogadas[computador]} :Computador')
        print('\033[31mDERROTA\033[m')
if jogador_choice == 3:
    if computador == 0:
        print(f'Jogador: {jogadas[jogador_choice-1]} x {jogadas[computador]} :Computador')
        print('\033[31mDERROTA\033[m')
    if computador == 1:
        print(f'Jogador: {jogadas[jogador_choice-1]} x {jogadas[computador]} :Computador')
        print('\033[34mVITÓRIA\033[m')
    if computador == 2:
        print(f'Jogador: {jogadas[jogador_choice-1]} x {jogadas[computador]} :Computador')
        print('\033[33mEMPATE\033[m')

