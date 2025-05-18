cadastro_jogador = {}
qtd_gols = list()
jogadores = list()
while True:
    print("-------"*5)
    cadastro_jogador['Nome'] = str(input('Nome do jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {cadastro_jogador['Nome']} jogou? '))
    for i in range(0, partidas):
        qtd_gols.append(int(input(f'Quantos gols na partida {i}: ')))
    cadastro_jogador['gols'] = qtd_gols[:]
    cadastro_jogador['total'] = sum(qtd_gols)
    jogadores.append(cadastro_jogador.copy())
    qtd_gols.clear()
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERROR! Digite Apenas os valores descritos (S/N)')
    if continuar == 'N':
        break
print('-=-='*7)
print('cod - nome        gols            total')
print('------'*7)
for k, v in enumerate(jogadores):
    print(f'{k}   {v['Nome']}       {v['gols']} {v['total']:>5}')
print('------'*7)
while True:
    dados = int(input('Mostrar dados de qual jogador? '))
    if dados == 999:
        break
    if dados >= len(jogadores):
        print(f'ERRO! não existe jogador com código {dados}! Tente novamente.')
    else:
        print(f'LEVANTAMENTO DOS DADOS DE {jogadores[dados]['Nome']}')
        for k, v in enumerate(jogadores[dados]['gols']):
            print(f'     => No jogo {k} fez {v} gols.')
        print('------'*7)
print(' <<< ENCERRADO >>>')