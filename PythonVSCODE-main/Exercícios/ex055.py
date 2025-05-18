maior = 0
menor = 0
lst = []
for p in range(1, 6):
    peso = float(input(f"{p}° Peso: "))
    lst += [peso]
print(f'Maior peso: {max(lst):.2f}Kg')
print(f'Menor peso: {min(lst):.2f}Kg')

