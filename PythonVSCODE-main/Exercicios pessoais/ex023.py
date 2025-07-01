pessoas = []
dado = []
maior = menor = 0
while True:
    dado.append(str(input("Nome: ")).strip())
    dado.append(float(input("Peso: ")))
    pessoas.append(dado[:])
    dado.clear()

    cont = " "
    while cont not in "SN":
        cont = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if cont == "N":
        break



for i in range(len(pessoas)):
    if i == 0:
        maior = menor = pessoas[i][1]
    else:
        if pessoas[i][1] > maior:
            maior = pessoas[i][1]
        if pessoas[i][1] < menor:
            menor = pessoas[i][1]

print('-=-='*10)
print(f'Ao total foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg -> ', end='')
for i in range(len(pessoas)):
    if maior == pessoas[i][1]:
        print(f'[ {pessoas[i][0]} ] ', end='')
print()
print(f'O menor peso foi de {menor:.1f}Kg -> ', end='')
for i in range(len(pessoas)):
    if menor == pessoas[i][1]:
        print(f'[ {pessoas[i][0]} ] ', end='')
print()

