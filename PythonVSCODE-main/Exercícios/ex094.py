pessoas_cadastradas = dict()
galera = list()

media_idade = 0
while True:
    pessoas_cadastradas['Nome'] = str(input('Nome: '))
    while True:
        pessoas_cadastradas['Sexo'] = str(input("Sexo [M/F]: ")).upper().strip()[0]
        if pessoas_cadastradas['Sexo'] in 'MF':
            break
        print('ERRO! Digite apenas os valores M ou F')
    pessoas_cadastradas['Idade'] = int(input('Idade: '))
    media_idade += pessoas_cadastradas['Idade']
    galera.append(pessoas_cadastradas.copy())

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Digite apenas os valores S para sim e N para não')
    if continuar == 'N':
        break
print("-=-=-="*15)
print(f' A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f' B) A média da idade é de {media_idade / len(galera):.2f} anos.')
print(f' C) As mulheres cadastradas foram ', end='')
for i in galera:
    if i['Sexo'] == 'F':
        print(f'{i['Nome']}', end=' → ')
print('FIM')
print(' D) Lista das pessoas que estão acima da média (Idade):')
for i in galera:
    if i['Idade'] > (media_idade / len(galera)):
        print(f'   -> Nome = {i['Nome']}; Sexo = {i['Sexo']}; Idade = {i['Idade']}')
print(' <<< ENCERRADO >>>')
                           
                          