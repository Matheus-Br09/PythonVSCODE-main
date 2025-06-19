def leiaDinheiro(n):
    valido = False
    while valido != True:
        ler = str(input(n)).strip().replace(',','.')
        if ler.isalpha() or ler.strip() == "" or ler.isalnum():
            print(f"\033[31mERRO: \"{ler}\" é um preço inválido!\033[m")
        else:
            valido = True
            return float(ler)
            
    