#def lin():
#    print('-'*30)

#lin()
#print("SALVE MALAK")
#lin()
#lin()
#print("Curso em Video Python")
#lin()
#lin()
#print("Matheus Alves")
#lin()



#def escrever(msg):
#    print('-'*30)
#    print(msg)
#    print('-'*30)


#escrever("Salve doidao")
#escrever("SISTEMA DE ALUNOS")


#def somar(a=0, b=0):
#    s = a + b
#    print(s)


#somar(5, 19)




#def contador(*num):
#    tam = len(num)
#    print(tam)


#contador(4, 7, 8)
#contador(4, 4, 6, 7, 8)




#Valores = [4, 7, 8, 2, 5]
#def dobra(lst):
#    pos = 0
#    while pos < len(lst):
#        lst[pos] *= 2
#        pos += 1


#print(Valores)
#dobra(Valores)
#print(Valores)




def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(6, 9, 8, 4, 3 ,5, 1, 2)