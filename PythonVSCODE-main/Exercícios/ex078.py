valores = []
maior = menor = 0
for i in range(0, 5):
    digito_usuario = valores.append(int(input("Digite um valor: ")))
    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]

print(f'O maior valor é {maior} localizado na posição ', end='')
for pos, num in enumerate(valores):
    if maior == num:
        print(f'{pos}...', end=' ')
print()
print(f'O menor número é {menor} localizado na posição ', end='')
for pos, num in enumerate(valores):
    if menor == num:
        print(f'{pos}...', end=' ')
print()

