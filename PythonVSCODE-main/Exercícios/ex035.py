comprimento1 = float(input('1° Comprimento: '))
comprimento2 = float(input('2° Comprimento: '))
comprimento3 = float(input('3° Comprimento: '))
if comprimento1 < comprimento2 + comprimento3 and comprimento2 < comprimento1 + comprimento3 and comprimento3 < comprimento2 + comprimento1:    
    print('PODE FORMAR um triângulo')
else:
    print('NÃO PODE formar um triângulo')