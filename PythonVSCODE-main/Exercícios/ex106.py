from time import sleep

print('\033[46m~' * 25, '')
print('  Sistema de Ajuda PyHELP ')
print('~' * 25, "\033[m")

def tamanho_doidao(msg):
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))


def PyHelp(com): 
    print('\033[47m', end='')
    print(help(com))
    print('\033[m', end='')



while True:
    questionated_function = str(input('Função ou Biblioteca > ')).lower()
    if questionated_function == "fim":
        print('\033[41m', end='')
        tamanho_doidao("ATÉ LOGO  ")
        print('\033[m')
        break
    else:
        print('\033[45m~' * 35, '')
        print(f'Acessando o manual do comando \'{PyHelp(questionated_function)}\' ')
        print('~' * 35, '\033[m')
        sleep(1)