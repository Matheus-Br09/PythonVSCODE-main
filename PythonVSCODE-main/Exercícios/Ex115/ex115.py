import createarchives
from time import sleep


opcao = 0
while opcao != 3:
    createarchives.tam_linhas("MENU PRINCIPAL")
    print("\033[35m1 - Ver pessoas cadastradas"\
          "\n2 - Cadastrar nova pessoa"\
          "\n3 - Sair do sistema\033[m")
    print('--'*20)

    opcao = createarchives.escolha_opcao("\033[34mSua opção: \033[m")

    if opcao == 1:
        createarchives.mostrar_cadastrados("PythonVSCODE-main/Exercícios/Ex115/cadastro_pessoas.txt")
        sleep(3)
    
    if opcao == 2:
        createarchives.tam_linhas("CADASTRO PESSOA")
        nome = str(input("Nome: "))
        try:
            idade = int(input("Idade: "))
        except (ValueError, TypeError):
            print("\033[31mERRO! Digite o valor corretamente...\033[m")
            sleep(1)
        else:
            createarchives.cadastro_pessoas(nome, idade)


createarchives.tam_linhas("<Volte Sempre>")