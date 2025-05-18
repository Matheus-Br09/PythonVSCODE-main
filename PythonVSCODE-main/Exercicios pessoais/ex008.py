valores = list()
maior = menor = 0

for i in range(0, 5):
    valor = int(input(f'Digite o valor {i+1}: '))
    valores.append(valor)
    if i == 0:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
print(f'O maior valor foi {maior} na(s) posição(ões) → ', end='')
for k, v in enumerate(valores):
    if v == maior:
        print(f'{k+1}...', end='')
print()
print(f'O menor valor foi {menor} na(s) posição(ões) → ', end='')
for k, v in enumerate(valores):
    if v == menor:
        print(f'{k+1}...', end='')
print()