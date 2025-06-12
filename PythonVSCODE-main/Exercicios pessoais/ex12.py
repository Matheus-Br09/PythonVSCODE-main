situacao_aluno = dict()

situacao_aluno["Nome"] = str(input("Nome do aluno: ")).strip()
situacao_aluno["Média"] = float(input("Média do aluno: "))
situacao_aluno["Situação"] = 'Aprovado'
if situacao_aluno["Média"] < 5:
    situacao_aluno['Situação'] = "Reprovado"
elif situacao_aluno["Média"] < 7:
    situacao_aluno["Situação"] = "Recuperação"

for k, v in situacao_aluno.items():
    print(f'{k}: {v}')