

def metade(n=1, ret_mo=False):
    if ret_mo == True:
        return moeda(n / 2)
    else:
        return n / 2

def dobro(n=1, ret_mo=False):
    if ret_mo == True:
        return moeda(n * 2)
    else:
        return n * 2

def aumentar(n, porc = 100, ret_mo=False):
    aumento = n + (n * (porc/100))
    if ret_mo == True:
        return moeda(aumento)
    else:
        return aumento

def diminuir(n = 0, porc = 100, ret_mo=False):
    reducao = n - (n * (porc/100))
    if ret_mo == True:
        return moeda(reducao)
    else:
        return reducao

def moeda(n=0):
    return f"R${n:>8.2f}".replace('.', ',')

def resumo(n=1, aum=1, red=1):
    print('------'*5)
    print('        RESUMO DO VALOR')
    print('------'*5)
    print(f"Preço analisado: {moeda(n)}")
    print(f"Dobro do preço:  {moeda(dobro(n))}")
    print(f"Metade do preço: {moeda(metade(n))}")
    print(f"{aum}% de aumento:  {moeda(aumentar(n, aum))}")
    print(f"{red}% de redução:  {moeda(diminuir(n, red))}")
    print('------'*5)