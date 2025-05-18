from time import sleep

def contador(inicio, fim, passo):
    print('-='*20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' → ', flush=True)
            cont += passo
            sleep(0.5)
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' → ', flush=True)
            cont -= passo
            sleep(0.5)
    print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de decidir tudo!!!')
ini = int(input("Início: "))
final = int(input("Fim: "))
steps = int(input("Passo: "))
if steps == 0:
    steps = 1
elif steps < 0:
    steps = abs(steps)
contador(ini, final, steps)