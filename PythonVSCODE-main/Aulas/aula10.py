#nome = str(input("Digite seu nome: "))
#if nome == 'Matheus':
#    print("Que nome lindo você tem!!")
#else:
#    print("Seu nome é tao normal")
#print(f'Bom dia {nome}!!')

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2

print(f'A sua média foi de {media: .1f}')
print('Parábens' if media >= 6 else "Estude mais!!")