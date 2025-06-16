valores = []
maior = 0
menor = 0
for i in range(0, 5):
    num = int(input(f"Digite um valor para a posição {i}: "))
    valores.append(num)
    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for k, v in enumerate(valores):
    if valores[k] == maior:
        print(f'{k}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for k, v in enumerate(valores):
    if valores[k] == menor:
        print(f'{k}... ', end='')
print()
