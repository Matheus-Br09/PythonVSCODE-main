print('=-=-'*6)
print("REGISTRADOR DE PESSOAS")
print('=-=-'*6)

idade = 0
sexo = ''
continuar = ''
mais_dezoito = m_menos_vinte = qtd_homens = 0

while True:
    idade = int(input('Idade: '))
    while True:
        sexo = str(input("Sexo: [M/F] ")).upper().strip()[0]
        if sexo in 'MF':
            break

    if idade >= 18:
        mais_dezoito += 1
    if sexo == 'F':
        if idade < 20:
            m_menos_vinte += 1
    if sexo == 'M':
        qtd_homens += 1

    while True:
        print("===="*6)
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        print('===='*6)
        if continuar in 'SN':
            break
    if continuar == 'N':
        break 

print('=-=-'*10)
print(f'Existem {mais_dezoito} PESSOAS com MAIS de 18 anos.')
print(f'Existem {m_menos_vinte} MULHERES com MENOS de 20 anos.')
print(f'Existem ao TOTAL {qtd_homens} HOMENS cadastrados')
print('=-=-'*10)