#def contador(i, f, p):
#    """ -> Faz uma P.A na tela
#    :param i: Primeiro número da P.A
#    :param f: último número da P.A
#    :param p: Passo dos dos números da P.A
#    :return: Sem retorno"""
#    c = i 
#    while c <= f:
#        print(f'{c}', end='..')
#        c += p
#    print('FIM!')
#contador(2, 10, 2)
#help(contador)





#def funcao():
#    n1 = 4
#    print(f'N1 dentro vale {n1}')
#n1 = 2
#funcao()
#print(f'N1 fora vale {n1}')


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')
    return s

r1 = somar(3, 2, 5)
r2 = somar(8, 4)
r3 = somar(7)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')