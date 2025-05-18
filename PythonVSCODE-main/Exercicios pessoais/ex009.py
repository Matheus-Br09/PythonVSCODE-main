valores = []

while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor ADICIONADO com sucesso!')
    else:
        print('Valor EXISTENTE, não será adicionado...')
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('DIGITE CORRETAMENTE...')
    if continuar == 'N':
        break

print(f'Valores adicionados: {sorted(valores)}')