pessoas = []
dado = []
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print('=-=-'*15)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
for i in range(0, len(pessoas)):
    if i == 0:
        maior = menor = pessoas[i][1]
    else:
        if pessoas[i][1] > maior:
            maior = pessoas[i][1]
        if pessoas[i][1] < menor:
            menor = pessoas[i][1]
print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')            
for num in pessoas:
    if num[1] == maior:
        print(f'[{num[0]}] ', end='')
print()
print(f'O menor peso foi de {menor:.1f}Kg. Peso de ', end='')
for num in pessoas:
    if num[1] == menor:
        print(f'[{num[0]}] ', end='')



