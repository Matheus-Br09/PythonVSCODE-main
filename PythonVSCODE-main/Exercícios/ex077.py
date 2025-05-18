tupla_braba = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON')

for i in tupla_braba:
    print(f'\nNa palavra {i} temos: ', end='')
    for letras in i:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')