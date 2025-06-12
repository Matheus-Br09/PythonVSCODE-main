pessoas = []
total_idade = 0
cadastro_pessoa = dict()
cont = ""
while True:
    cadastro_pessoa["Nome"] = str(input("Nome: ")).strip()

    while True:
        cadastro_pessoa["Sexo"] = str(input("Sexo: [M/F] ")).strip().upper()[0]
        if cadastro_pessoa["Sexo"] in "MF":
            break
        print("DIGITE O SEXO CORRETAMENTE!")

    cadastro_pessoa["Idade"] = int(input("Idade: "))
    total_idade += cadastro_pessoa["Idade"]
    pessoas.append(cadastro_pessoa.copy())
    cont = " " 
    while cont not in "SN":
        cont = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if cont == "N":
        break
 
print(f' - O grupo tem {len(pessoas)} pessoas.')
print(f' - A média de idade é de {total_idade / (len(pessoas)):.2f}')
print(f' - As mulheres cadastradas foram: ', end='')
for i in range(0, len(pessoas)):
    if pessoas[i]["Sexo"] == "F":
        print(f'{pessoas[i]["Nome"]}', end='  ')
print()
print(' - Lista das pessoas com nome acima da média')

for i in pessoas:
    if i["Idade"] > total_idade / len(pessoas):
        print(f'Nome = {i["Nome"]}; Sexo = {i["Sexo"]}; Idade = {i["Idade"]}')
    print()

print("<<< ENCERRADO >>>")
