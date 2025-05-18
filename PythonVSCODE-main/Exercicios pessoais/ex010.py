valores = []
pares = []
impares = []

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print("Digite o valor corretamente...")
    if continuar == 'N':
        break

for i in range(0, len(valores)):
    if valores[i] % 2 == 0:
        pares.append(valores[i])
    else:
        impares.append(valores[i])

print(f'Os valores digitados foram: {valores}')
print(f'Os valores pares são: {sorted(pares)}')
print(f'Os valores ímpares são: {sorted(impares)}')