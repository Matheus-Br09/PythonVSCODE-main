soma = 0
for c in range(1, 7):
    num = int(input(f"Digite o {c}° valor: "))
    if num % 2== 0:
        soma += num
print(f'A soma dos valores pares é de {soma}')