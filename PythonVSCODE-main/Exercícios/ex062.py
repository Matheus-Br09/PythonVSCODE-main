print('GERADOR DE P.A')
print("=-"*10)

contagem_decimo = 0
mais = 9
cont = 0
total = 0
primeiro_termo = int(input("Primeiro termo: "))
razao = int(input('Razão: '))

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{primeiro_termo} ', end=' → ')
        cont += 1
        primeiro_termo += razao
    print("PAUSA")
    mais = int(input("Quantos mais você quer? [0 Para finalizar] "))
print("FIM")