from random import randint

computer_thinks = randint(0, 5)
print('Pensei em um número... adivinhe qual !!!')
escolha_jogador = int(input('Digite um número: '))
if escolha_jogador >= 0 or escolha_jogador <= 5:
    if escolha_jogador == computer_thinks:
        print('VOCÊ ACERTOU')
    if escolha_jogador != computer_thinks:
        print('VOCÊ ERROU... tente novamente se quiser')
if escolha_jogador < 0 or escolha_jogador > 5:
    print("Digite um valor entre o limite de 0 e 5")
    

