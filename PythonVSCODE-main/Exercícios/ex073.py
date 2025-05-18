tp_brasileirao = ('Flamengo', 'Palmeiras', 'Fluminense', 'Ceará SC', 'Cruzeiro', 'Bragantino',
                  'Corinthians', 'Vasco', 'Juventude', 'Internacional', 'Mirassol', 'Botafogo',
                  'Fortaleza', 'Santos', 'Vitória', 'Grêmio', 'São Paulo', 'Bahia', 'Atlético MG',
                  'Sport Recife')
print('=-=-'*15)
print(f'Os primeiros 5 colocados são', end='')
for i in range(0, 6):
    print(f', {tp_brasileirao[i]}', end='')
print('.')
print('=-=-'*15)
print('Os 4 últimos colocados são', end='')
for i in range(4, 0, -1):
    print(f', {tp_brasileirao[-i]}', end='')
print('.')
print('=-=-'*15)
print(f'Times em ordem Alfabética: {sorted(tp_brasileirao)}')
print('=-=-'*15)
print(f'O Corinthians está na posição {tp_brasileirao.index("Corinthians")}')
print('=-=-'*15)
