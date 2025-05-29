def leiaInt(name):
    while True:
        num = str(input(name))
        if num.isdigit():
            num = int(num)
            return num
            break
        else:
            print("\033[31mDIGITE O VALOR CORRETAMENTE\033[m")



num = leiaInt("Digite um número: ")
print(f'Você digitou o número {num}')