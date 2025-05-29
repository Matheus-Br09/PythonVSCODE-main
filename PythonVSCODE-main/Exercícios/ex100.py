from random import randint

numeros = []

def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        lista.append(randint(1, 10))
        print(f'{lista[i]} ', end='')
    print(' PRONTO!')


sorteia(numeros)

def somarPar(num):
    soma = 0
    for i in num:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores PARES de {num}, temos {soma}')


somarPar(numeros)
