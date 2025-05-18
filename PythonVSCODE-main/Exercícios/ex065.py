numeros = 0
soma = 0
cont = 0
media = 0
#maior = 0
lst = []
menor = 0
continuar = ""
while continuar != "N":
    numeros = int(input('Digite um valor: '))
    soma += numeros
    lst += [numeros]
    cont += 1
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
media = soma / cont
print(f'A média dos {cont} números é {media:.2f}')
print(f"O MAIOR NÚMERO: {max(lst)}")
print(f"O MENOR NÚMERO: {min(lst)}")