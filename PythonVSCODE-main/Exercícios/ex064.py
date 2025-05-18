soma_numeros = 0
valor = 0
cont = 0
while valor != 999:
    cont += 1
    soma_numeros += valor
    valor = int(input("Digite um valor: "))
print(f'Você digitou {cont} valores e a soma entre eles foi {soma_numeros}')
