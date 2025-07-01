ficha = list()

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media_nota = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media_nota])
    cont = " "
    while cont not in "SN":
        cont = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if cont == 'N':
        break

print('-=-='*10)
print('No. NOME        MÉDIA')
print('-----'*5)
for n, v in enumerate(ficha):
    print(f'{n}   {v[0]:<8}     {v[2]:>2}')
print('-----'*5)
while True:
    mostrar_conteudo = int(input("Mostrar notas de qual aluno? (999 para interrompe): "))
    if mostrar_conteudo == 999:
        break
    elif mostrar_conteudo > len(ficha)-1 or mostrar_conteudo < 0:
        print(f'ERRO! Digite os valores corretamente!!!')
    else:
        print(f'As notas de {ficha[mostrar_conteudo][0]} são {ficha[mostrar_conteudo][1]}')
    print('-----'*5)


print("-=-=-=", "< ATÉ LOGO >", "=-=-=-")
    