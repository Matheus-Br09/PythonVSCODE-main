from time import sleep
ficha_escolar = list()

while True:
    nome_aluno = str(input('Nome do Aluno: ')).strip()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha_escolar.append([nome_aluno, [nota1, nota2], media])
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('=-=-'*16)
print('No. Nome        Media')
print('--------'*5)
for pos, values in enumerate(ficha_escolar):
    print(f'{pos:<4}{values[0]:<2}      {values[2]:^10.1f}')
print('--------'*5)

ver_notas = int()
while True:
    ver_notas = int(input('Mostrar notas de qual aluno? [999 para interromper] '))
    if ver_notas == 999:
        break
    if ver_notas > len(ficha_escolar)-1:
        print('VALOR FORA DA LISTAGEM')
    else:
        print(f'As notas de {ficha_escolar[ver_notas][0]} são {ficha_escolar[ver_notas][1]}')
        print('--------'*5)
        sleep(1)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')