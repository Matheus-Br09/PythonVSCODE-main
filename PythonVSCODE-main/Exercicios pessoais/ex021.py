valores = []
while True:
    valores.append(int(input("Digite um valor: ")))
    cont = " "
    while cont not in "SN":
        cont = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if cont == "N":
        break
print('-=-='*13)
print(f'Números digitados: {valores}')
print('-=-='*13)
print(f'A) O total de números digitados foi de {len(valores)}')
print(f'B) Os números ordenados em decrescente é {sorted(valores, reverse=True)}')
if 5 in valores:
    print(f'O valor 5 está presente e nas posições ', end='')
    for k, v in enumerate(valores):
        if v == 5:
            print(f'{k+1}... ', end='')
    print()
else:
    print(f'O número 5 NÃO está presente.')