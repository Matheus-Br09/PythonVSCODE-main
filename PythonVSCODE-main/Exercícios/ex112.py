def leiaInt(n=0):
    while True:
        try:
            n = int(input("Digite um Inteiro: "))
        except (TypeError, ValueError):
            print('\033[31mERRO: por favor, digite um número Inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31mO usuário preferiu não digitar esse número\033[m')
            n = 0
            return n
        else:
            return n


def leiaFloat(n=0):
    while True:
        try:
            n = int(input("Digite um Real: "))
        except (TypeError, ValueError):
            print("\033[31mERRO: por favor, digite um número Real válido\033[m")
        except KeyboardInterrupt:
            print("\033[31mO usuário preferiu não digitar esse número\033[m")
            n = 0
            return n
        else:
            return n




inteiro = leiaInt()
real = leiaFloat()
print(f'O número Inteiro digitado foi {inteiro} e o Real foi {real}')


