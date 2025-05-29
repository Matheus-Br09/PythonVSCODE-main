def ficha(jogador="<desconhecido>", gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


nome_jogador = str(input("Nome do jogador: ")).strip()
num_gols = str(input('Número de gols: '))
if num_gols.isnumeric():
    num_gols = int(num_gols)
else:
    num_gols = 0
if nome_jogador == '':
    ficha(gols=num_gols)
else:
    ficha(nome_jogador, num_gols)
