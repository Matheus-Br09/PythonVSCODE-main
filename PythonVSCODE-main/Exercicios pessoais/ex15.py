dados_jogador = dict()

dados_jogador["Nome"] = str(input("Nome do jogador: "))
qtd_partidas = int(input("Quantas partidas joelson jogou? "))
dados_jogador["Gols"] = []
for i in range(0, qtd_partidas):
    gols = int(input(f"Quantos gols na partida {i}? "))
    dados_jogador["Gols"] += [gols]
dados_jogador["Total"] = sum(dados_jogador["Gols"])
print('-=-='*10)
print(dados_jogador)
print('-=-='*10)
for k, v in dados_jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=-='*10)
print(f'O jogador {dados_jogador["Nome"]} jogou {qtd_partidas} partidas.')
for v, i in enumerate(dados_jogador["Gols"]):
    print(f'   => Na partida {v}, fez {dados_jogador["Gols"][v]} gols.')
print(f'Foi um total de {dados_jogador["Total"]} gols.')
