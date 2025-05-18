# lanche.APPEND() -> adiciona um valor
# lanche.INSERT() -> adiciona um valor, porém na posição zero
# DEL lanche[3]
# lanche.POP(3)
# lanche.REMOVE("Pitissa")
# valores = list(range(4, 11))
# valores = [8, 2, 5, 9, 3, 0]
# valores.SORT()
# valores.sort(REVERSE=TRUE)
# len(valores)

#num = [2, 5, 9, 1]
#num[2] = 4
#num.append(7)
#num.sort(reverse=True)
#num.insert(2, 2)
#if 6 in num:
#    num.remove(6)
#else:
#    print('Ta drogado maluco? nem existe esse número aqui')
#print(num)
#print(f'Essa lista tem {len(num)} elementos')

#valores = []
#for cont in range(0, 5):
#    valores.append(int(input("Digite um valor: ")))
#for c, valor in enumerate(valores):
#    print(f'na posição {c+1} encontrei o valor {valor}!')
#print('Cheguei ao final da lista!!!')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')