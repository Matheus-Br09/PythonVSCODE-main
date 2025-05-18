from random import randint
from time import sleep

jogadas_dado = {'Jogador 1': randint(1, 6),
                'Jogador 2': randint(1, 6),
                'Jogador 3': randint(1, 6),
                'Jogador 4': randint(1, 6)}
for k, v in jogadas_dado.items():
    print(f'O {k} tirou {v} no Dado.')
    sleep(0.5)
print('-------'*6)
print('=== Ranking dos Jogadores ===')
ranking = sorted(jogadas_dado.items(), reverse=True, key=lambda x:x[1])
for k, v in enumerate(ranking):
    print(f'{k+1}° Lugar: {v[0]} com {v[1]}')
    sleep(1)
    