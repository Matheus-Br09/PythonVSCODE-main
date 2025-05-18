listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
            'Compasso', 9.90, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('--------'*4)
print('        Lista de Produtos')
print('--------'*4)
for itens in range(0, len(listagem), 2):
    print(f'{listagem[itens]:.<34}', end='')
    print(f'R$ {listagem[itens+1]:>7.2f}')