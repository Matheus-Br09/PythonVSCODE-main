from random import randint

tp_numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for i in range(0, 5):
    print(tp_numeros[i], end='  ')
print()
print(f'O maior valor sorteado: {max(tp_numeros)}')
print(f'O menor valor sorteado: {min(tp_numeros)}')