print('GERADOR DE P.A')
print('=-'*9)
prim_termo = int(input('Primeiro Termo: '))
raz_termo = int(input('Razão do Termo: '))
contagem_decimo = 0
while contagem_decimo < 10:
    print(f'{prim_termo}', end=' → ')
    contagem_decimo += 1
    prim_termo += raz_termo
print('FIM')