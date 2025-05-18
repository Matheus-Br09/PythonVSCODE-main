nome_produto = nome_barato = ''
preco_produto = mais_barato = mais_mil = total = quant = 0

print('==='*8)
print('     LOJA DO KBEÇA')
print('==='*8)

while True:
    print('---'*6)
    nome_produto = str(input('Nome do produto: ')).strip()
    preco_produto = float(input('Preço: R$'))
    print('---'*6)

    total += preco_produto
    quant += 1

    if preco_produto > 1000:
        mais_mil += 1

    if quant == 1:
        mais_barato = preco_produto
    else:
        if preco_produto < mais_barato:
            mais_barato = preco_produto
            nome_barato = nome_produto
            
    continuar = ' '
    while continuar not in 'SN':
        print('==='*8)
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('==='*8)    
    if continuar == 'N':
        break
    

print(f'O total das compras é de R${total:.2f}')
print(f'Nas compras, possuem {mais_mil} que custam mais de R$1000,00')
print(f'O produto mais barato foi {nome_barato} custando R${mais_barato:.2f}')

