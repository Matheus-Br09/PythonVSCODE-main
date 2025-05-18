numero_tab = cont = 0

while True:
    numero_tab = int(input('Qual tabuada você quer ver? '))
    if numero_tab < 0:
        break
    print('--'*6)
    for i in range(1, 11):
        print(f'{numero_tab} x {i} = {numero_tab*i}')
    print('--'*6)
    
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')