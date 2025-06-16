valores = []
while True:
    num = int(input("Digite um valor: "))
    if num in valores:
        print('NÚMERO JÁ ADICIONADO!!! não vou adicionar...')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    
    cont = " "
    while cont not in "SN":
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('-=-='*15)
print(f'Você digitou os valores {sorted(valores)}')
