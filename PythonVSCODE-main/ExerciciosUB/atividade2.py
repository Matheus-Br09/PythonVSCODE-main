from time import sleep

dic_produtos = dict()
produtos_armazenados = list()

while True:
    print('1 - Cadastrar produto \n' \
          '2 - Buscar produtos \n' \
          '3 - Listar produtos \n' \
          '4 - Sair do PROGRAMA')
    opcao = int(input('Sua escolha: '))

    if opcao == 1:

        print('-=-='*10)
        dic_produtos['Nome Do Produto'] = str(input('Nome do produto: ')).strip()
        dic_produtos['Preço'] = float(input('Preço do produto: R$'))
        dic_produtos['Quantidade'] = int(input('Quantidade em estoque: '))
        dic_produtos['Categoria'] = str(input('Categoria do produto: ')).strip() 
        print('-=-='*10)
        produtos_armazenados.append(dic_produtos.copy())

    elif opcao == 2:

        print('-=-='*10)
        for p, v in enumerate(produtos_armazenados):
            print(f'{p} → {v["Nome Do Produto"]}')
        print("-----"*8)
        index_finder = int(input('Digite a posição do produto: '))
        tamanho = len(produtos_armazenados)
        if 0 <= index_finder < tamanho:
            print(f'Nome do Produto: {produtos_armazenados[index_finder]['Nome Do Produto']}')
            print(f'Preço do Produto: {produtos_armazenados[index_finder]['Preço']}')
            print(f'Quantidade em estoque: {produtos_armazenados[index_finder]['Quantidade']}')
            print(f'Categoria do produto: {produtos_armazenados[index_finder]['Categoria']}')
            sleep(2)
        else:
            print('Indíce Inválido!!!')
        print('-=-='*10)
        sleep(1)
    elif opcao == 3:
        if len(produtos_armazenados) == 0:
            print("\033[31mNenhum Produto Cadastrado!!\033[m")
        else:
            print("----"*15)
            for k, v in enumerate(produtos_armazenados):
                print(f'índice: {k}')
                print(f' -Nome: {produtos_armazenados[k]['Nome Do Produto']} \n',
                    f'-Preço: R${produtos_armazenados[k]['Preço']} \n',
                    f'-Quantidade: {produtos_armazenados[k]['Quantidade']} \n',
                    f'-Categoria: {produtos_armazenados[k]['Categoria']} \n')
                sleep(1)
            print('----'*15)
    elif opcao == 4:
        break

    else:
        print("OPÇÃO INVÁLIDA")
        print()

print("<<< PROGRAMA ENCERRADO >>>")

