valor = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
valor3 = int(input('Digite mais um valor: '))
valor4 = int(input('Digite o último valor: '))
tp_numeros = (valor, valor2, valor3, valor4)
print(f'O valor 9 apareceu {tp_numeros.count(9)} vezes')

if 3 in tp_numeros:
    print(f'O valor 3 apareceu na {tp_numeros.index(3)+1}a Posição')
else:
    print('Não foi digitado o número 3')

print(f'Os números pares digitados foram:', end='')
for pos, med in enumerate(tp_numeros):
    if med % 2 == 0:
        print(f' {med} ', end='')