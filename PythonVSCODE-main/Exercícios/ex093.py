cadastro_jogador = {'Nome': '', 'gols': 0, 'total': 0}

cadastro_jogador['Nome'] = str(input('Nome do jogador: ')).strip()
partidas = int(input(f'Quantas partidas {cadastro_jogador['Nome']} jogou? '))
qtd_gols = list()
cadastro_jogador['total'] = 0
for i in range(0, partidas):
    qtd_gols.append(int(input(f'Quantos gols na partida {i}: ')))
    cadastro_jogador['total'] += qtd_gols[i]

cadastro_jogador['gols'] = qtd_gols[:]
print('-=-='*16)
print(cadastro_jogador)
print('-=-='*16)
for k, v in cadastro_jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-='*16)
for i, v in enumerate(qtd_gols):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {cadastro_jogador['total']} gols.')