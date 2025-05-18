entrada = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8]
id_num = 0
for pos, num in enumerate(entrada):
    if num != id_num:
        id_num = entrada[pos]
    elif num == id_num:
        entrada.pop(entrada[pos])
print(entrada)