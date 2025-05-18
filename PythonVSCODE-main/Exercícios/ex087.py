matriz = [[0, 0, 0], 
          [0, 0, 0], 
          [0, 0, 0]]
maior = somaPar = somaTerCol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        somaTerCol += matriz[l][2]
print('=-=-'*14)
for l in range(0,3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]} ]', end='')
    print()

print(f'A soma dos pares é {somaPar}')
print(f'A soma da terceira coluna inteira é {somaTerCol}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')