from random import randint
from time import sleep

print("---"*8)
print("   JOGOS DA MEGA SENA")
print("---"*8)

jogos = []
sorteio = int(input("Quantos jogos você quer que eu sorteie? "))
print("-=-=", f"SORTEANDO {sorteio} JOGOS", "=-=-")
for i in range(0, sorteio):
    jogadas = []
    while len(jogadas) < 6:
        aleatorio = randint(1, 60)
        if aleatorio not in jogadas:
            jogadas.append(aleatorio)
    jogos.append(sorted(jogadas[:]))
 
for i in range(0, (len(jogos))):
    print(f'Jogo {i+1}: {jogos[i]}')
    sleep(0.7)
print('-=-=-=', '< BOA SORTE >', '=-=-=-')


