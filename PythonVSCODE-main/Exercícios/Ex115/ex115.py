import os
from time import sleep

def tam_linhas(msg):
    print('--'*(len(msg) + 6))
    print(f'             {msg}')
    print('--'*(len(msg) + 6))

conteudo = ""
opcao = 0
while opcao != 3:
    tam_linhas("MENU PRINCIPAL")
    print("1 - Ver pessoas cadastradas"\
          "\n2 - Cadastrar nova pessoa"\
          "\n3 - Sair do sistema")
    print('--'*20)

    try:
        opcao = int(input("Sua opção: "))
    except (TypeError, ValueError):
        print("\033[31mERRO! Digite uma opção válida!\033[m")
        sleep(1)
    else:
        if opcao > 3 or opcao < 1:
            print("\033[31mERRO! Digite uma opção válida!\033[m")
            sleep(1)
        else:
            if opcao == 3:
                break
    print('--'*20)
    print(f'                 OPÇÃO {opcao}')
    print('--'*20)
    if opcao == 1:
        try:
            f = open("PythonVSCODE-main/Exercícios/Ex115/cadastro_pessoas.txt", "r")
            conteudo = f.read()
        except (FileNotFoundError):
            print("\033[31mArquivo não existente! Crie um cadastro para continuar...\033[m")
            sleep(1)
        else:
            print('--'*20)
            print(conteudo)
            print('--'*20)
            sleep(1)       
    
    if opcao == 2:
        tam_linhas("CADASTRO PESSOA")
        try: 
            f = open("PythonVSCODE-main/Exercícios/Ex115/cadastro_pessoas.txt", "x")
        except (FileExistsError):
            continue
        finally:
            nome = str(input("Nome: "))
            try:
                idade = int(input("Idade: "))
            except (ValueError, TypeError):
                print("\033[31mERRO! Digite o valor corretamente...\033[m")
                sleep(1)
            else:
                with open("PythonVSCODE-main/Exercícios/Ex115/cadastro_pessoas.txt", "a") as f:
                    f.write(f"{nome:<20}         {idade} Anos" + "\n")



tam_linhas("Volte Sempre")