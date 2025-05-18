def maior(*num):
    cont = maior = 0
    print("\nAnalisando os valores passados...")
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(6, 9, 2, 5, 2, 1)
                