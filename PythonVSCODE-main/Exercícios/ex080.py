valores = []
for i in range(0, 5):
    digito_usuario = int(input(f'Digite um valor: '))
    if i == 0 or digito_usuario > valores[-1]:
        valores.append(digito_usuario)
    else:
        pos = 0
        while pos < len(valores):
            if pos <= valores[pos]:
                valores.insert(pos, digito_usuario)
                break
            pos += 1
print(valores)
            

    