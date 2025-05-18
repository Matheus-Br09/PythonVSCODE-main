id_aluno = dict()

id_aluno['Nome'] = str(input('Nome do aluno: ')).strip()
id_aluno['Média'] = float(input('Média do aluno: '))
id_aluno['Situação'] = ''
if id_aluno['Média'] > 7:
    id_aluno['Situação'] = 'APROVADO'
elif id_aluno['Média'] < 5:
    id_aluno['Situação'] = 'REPROVADO'
else:
    id_aluno['Situação'] = 'RECUPERAÇÃO'
print('=-=-'*8)
for k, v in id_aluno.items():
    print(f'{k} é igual a {v}')