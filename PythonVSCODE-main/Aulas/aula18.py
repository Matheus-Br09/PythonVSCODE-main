#pessoas = {'nome': "Matheus", 'Sexo': 'M', 'Idade': 18}
#pessoas['peso'] = 98.7
#for k, v in pessoas.items():
#    print(f'{k} = {v}')

#brasil = list()
#estado = {'uf': 'Pernambuco', 'sigla': 'PE'}
#stado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
#brasil.append(estado)
#brasil.append(estado2)
#print(brasil[1]['uf'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()