print(f'Sequência de fibonnaci')
primeiro_valor = 0
segundo_valor = 1
t3 = 0
print(f'{primeiro_valor}\n'
      f'{segundo_valor}')
for i in range(500):
    t3 = primeiro_valor + segundo_valor
    print(f'{t3}')
    primeiro_valor = segundo_valor
    segundo_valor = t3

