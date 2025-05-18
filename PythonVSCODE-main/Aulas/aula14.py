#c = 1
#while c < 11 :
#    print(c)
#    c = c + 1
    
#print('fim')

n = 1
cont_par = 0
cont_impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        cont_par += 1
        if n == 0:
            cont_par -= 1
    else:
        cont_impar += 1
print(f'Ao todo, existem {cont_par} números pares')
print(f'Ao todo, existem {cont_impar} números impares')