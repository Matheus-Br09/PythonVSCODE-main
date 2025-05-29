def fatorial(numero=1, show=False):
    """-> Calcula o fatorial de um número.
    :param numero: Número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de um numero"""   
    f = 1           
    for c in range(numero, 0, -1):
        if show == True:
            print(f'{c}', end=' ')
            if c != 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f


print(fatorial(5, False))