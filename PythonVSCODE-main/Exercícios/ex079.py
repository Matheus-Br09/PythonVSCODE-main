valores = []

while True:
    digito_usuario = int(input('Digite um valor: '))
    if digito_usuario not in valores:
        valores.append(digito_usuario)
        print(f'Número adicionado com sucesso...')
    else:
        print(f'Número DULPLICADO! Não adicionado a lista...')

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
valores.sort()
print(f'VocÊ adicionou os valores {valores}')