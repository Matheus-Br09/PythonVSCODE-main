jogadores_Cadastrados = []
dados_jogador = dict()

while True:
    print('---'*10)
    dados_jogador["Nome"] = str(input("Nome do jogador: "))
    qtd_partidas = int(input(f"Quantas partidas {dados_jogador['Nome']} jogou? "))
    dados_jogador["Gols"] = []
    for i in range(0, qtd_partidas):
        gols = int(input(f"Quantos gols na partida {i+1}? "))
        dados_jogador["Gols"] += [gols]
    dados_jogador["Total"] = sum(dados_jogador["Gols"])
    jogadores_Cadastrados.append(dados_jogador.copy())
    cont = " "
    while cont not in "SN":
        cont = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if cont == "N":
        break

print('-=-='*10)
print(f'cod  nome       gols          total')
print('---' * 13)
for k, v in enumerate(jogadores_Cadastrados):
    print(f'{k}  {v["Nome"]}     ', end='')
    print(f'{v["Gols"]}', end='')
    print(f'     {v["Total"]}')
print('---'*13)
while True:
    escolha = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if escolha == 999:
        break
    if escolha >= len(jogadores_Cadastrados):
        print(f"ERRO! Não existe jogador com código {escolha}! Tente Novamente.")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {jogadores_Cadastrados[escolha]["Nome"]}")
        for k, v in enumerate(jogadores_Cadastrados[escolha]["Gols"]):
            print(f'   No jogo {k+1} fez {v} gols.')

print('<<<( ENCERRADO )>>>')