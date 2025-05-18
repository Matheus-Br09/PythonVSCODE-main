numero = int(input("Digite o valor: "))
print('[1] BINÁRIO '
'[2] OCTAL '
'[3] HEXADECIMAL')
escolha_base = int(input('Converter para qual base? '))
if escolha_base == 1:
    print(f'{numero} em BINÁRIO fica: {bin(numero)[2:]}')
elif escolha_base == 2:
    print(f'{numero} em OCTAL fica: {oct(numero)[2:]}')
elif escolha_base == 3:
    print(f'{numero} em HEXADECIMAL fica: {hex(numero)[2:]}')
else:
    print("Digite o valor corretamente!!!")