lista_geral = []
pares = lista_geral[:]
impares = lista_geral[:]

while True: 
    digito_usuario = int(input('Digite um valor: '))
    lista_geral.append(digito_usuario)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input("Quer continuar? [S/N] ")).upper().strip()
    if continuar == 'N':
        break

for i in range(0, len(lista_geral)):
    if lista_geral[i] % 2 == 0:
        pares.append(lista_geral[i])
    elif lista_geral[i] % 2 == 1:
        impares.append(lista_geral[i])

print(f'Os números digitados foram: {lista_geral}')
print(f'Os números pares digitados foram: {pares}')
print(f'Os números ímpares digitados foram: {impares}')