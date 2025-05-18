valores = [[], []]
for i in range(1, 8):
    num_digito = int(input(f'Digite o {i}° valor: '))
    if num_digito % 2 == 0:
        valores[0].append(num_digito)
    if num_digito % 2 == 1:
        valores[1].append(num_digito)
print('=-=-'*15)
print(f'Os valores ÍMPARES digitados foram {sorted(valores[0])}')
print(f'Os valores PARES digitados foram {sorted(valores[1])}')