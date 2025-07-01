matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

somaPar = somaTerceiraCol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Valor para posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        somaTerceiraCol += matriz[l][2]
print('-=-='*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ', end='')
    print()


print(f'A soma de todos os valores pares digitados é: {somaPar}')
print(f'A soma dos valores da terceira coluna é: {somaTerceiraCol}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
      
        