valores = []
lista_par = []
lista_impar = []

while True:
    valores.append(int(input("Digite um número: ")))
    cont = " "
    while cont not in "SN":
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont == "N":
        break

for i in valores:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)

print('-=-='*13)
print(f'Os valores digitados foram: {valores}')
print('-=-='*13)
print(f'Valores pares digitados: {sorted(lista_par)}')
print(f'Valores ímpares digitados: {sorted(lista_impar)}')