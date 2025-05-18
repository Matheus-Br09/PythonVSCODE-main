valores = []
while True:
    digito_usuario = int(input('Digite um valor: '))
    valores.append(digito_usuario)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('=-=-'*12)
print(f'Foram digitados e adicionados {len(valores)} na lista!')
print(f'A lista em forma decrescente é: {sorted(valores, reverse=True)}')
if 5 in valores:
    print(f'O número 5 foi digitado e está na posição ', end='')
    for pos, num in enumerate(valores):
        if num == 5:
            print(f'{pos+1}... ', end='')
    print()
else:
    print("O número 5 NÃO foi digitado")
print('=-=-'*12)
