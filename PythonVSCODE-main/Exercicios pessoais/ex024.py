valores = [[], [], []]
for i in range(0, 7):
    valores[0].append(int(input(f"Digite o {i+1}° Valor: ")))
for v in valores[0]:
    if v % 2 == 0:
        valores[1].append(v)
    else:
        valores[2].append(v)
print(f'Valores digitados: {valores[0]}')
print(f'Valores pares digitados: {sorted(valores[1])}')
print(f'Valores ímpares digitados: {sorted(valores[2])}')