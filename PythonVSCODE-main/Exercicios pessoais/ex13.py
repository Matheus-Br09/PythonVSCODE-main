from random import randint
from operator import itemgetter


salva_Dados = {}
jogada_dados = {"Jogador 1": randint(1, 6), 
                "Jogador 2": randint(1, 6),
                "Jogador 3": randint(1, 6),
                "Jogador 4": randint(1, 6)
                }


for k, v in jogada_dados.items():
    print(f'O {k} tirou {v}')
print('~' * 30)
salva_Dados = sorted(jogada_dados.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(salva_Dados):
    print(f'{k+1}° lugar: {v[0]} com {v[1]}')

