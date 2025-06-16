from random import randint

def lanca_Dado():
    valores = []
    for i in range(0, 100):
        a = randint(1, 6)
        valores.append(a)
    return valores


def qtd_Vezes(msg):
    elementos = {1: 0,
                 2: 0,
                 3: 0,
                 4: 0,
                 5: 0,
                 6: 0}
    for i in msg:
        if i in elementos:
            elementos[i] += 1
    return elementos


for k, v in qtd_Vezes(lanca_Dado()).items():
    print(f'O valor {k} apareceu {v} vezes')