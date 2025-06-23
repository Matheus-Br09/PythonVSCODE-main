from time import sleep

def mostrar_cadastrados(msg):
        try:
            f = open(msg, "r")
            conteudo = f.read()
        except (FileNotFoundError):
            print("\033[31mArquivo não existente! Crie um cadastro para continuar...\033[m")
        else:
            print('--'*20)
            print(conteudo)
            print('--'*20)


def cadastro_pessoas(nome="", idade=0):
    try: 
        f = open("PythonVSCODE-main/Exercícios/Ex115/cadastro_pessoas.txt", "x")
    except (FileExistsError):
        print('',end='')
    finally:
         with open("PythonVSCODE-main/Exercícios/Ex115/cadastro_pessoas.txt", "a") as f:
              f.write(f"{nome:<20}         {idade} Anos" + "\n")


def tam_linhas(msg):
    print('--'*(len(msg) + 6))
    print(f'             {msg}')
    print('--'*(len(msg) + 6))


def escolha_opcao(msg):

    try:
        opcao = int(input(msg))
    except (TypeError, ValueError):
        print("\033[31mERRO! Digite uma opção válida!\033[m")
        sleep(1)
    else:
        if opcao > 3 or opcao < 1:
            print("\033[31mERRO! Digite uma opção válida!\033[m")
            sleep(1)
        else:
            print('--'*20)
            print(f'                 OPÇÃO {opcao}')
            print('--'*20)
            return opcao
            