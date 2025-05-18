sexo = ''
while sexo != 'MF':
    sexo = str(input('Sexo [M, F]: ')).upper().strip()
    if sexo in 'MF':
        if sexo == 'M':
            print(f'Você é do sexo: MASCULINO')
            break
        if sexo == 'F':
            print(f'Você é do sexo: FEMININO')
            break
    else:
        print('\033[31mDIGITE O VALOR CORRETAMENTE\033[m')
