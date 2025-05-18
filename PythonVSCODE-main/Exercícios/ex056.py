media_idade = 0
mul_m20 = 0
hom_mVelho = 0
nome_mVelho = ''
for i in range(1, 5):
    print('=='*5,f'{i}° PESSOA ', '=='*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()
    media_idade += idade
    if i == 1 and sexo in 'Mm':
        hom_mVelho = idade
        nome_mVelho = nome
    if sexo in 'Mm' and idade > hom_mVelho:
        hom_mVelho = idade
        nome_mVelho = nome
    if i == 1 and sexo in 'Ff':
        mul_m18 = idade
    if sexo in 'Ff' and idade < 20:
        mul_m20 += 1

print(f'A média de idade do grupo é: {media_idade/4:.1f}')
print(f'O homem mais velho tem {hom_mVelho} e se chama {nome_mVelho}')
print(f'Existe {mul_m20} mulheres abaixo dos 20 anos')