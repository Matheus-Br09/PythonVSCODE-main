from random import randint
from time import sleep

print("---"*9)
print('     JOGO DA MEGA SENA')
print("---"*9)
jogos = []
qtd_jogos = int(input("Quantos jogos você quer que eu sorteie? "))
print('-=-=-=', f'SORTEANDO {qtd_jogos} JOGOS', '=-=-=-')
for jogo in range(1, qtd_jogos+1):
    print(f'Jogo {jogo}: ', end='')
    for sorteados in range(0, 6):
        num_sort = randint(0, 60)    
        if num_sort not in jogos:
            jogos.append(num_sort)    
    print(f'{sorted(jogos)}')
    sleep(0.8)
    jogos.clear()
print('-='*4, '< BOA SORTE! >', '=-'*4)
    