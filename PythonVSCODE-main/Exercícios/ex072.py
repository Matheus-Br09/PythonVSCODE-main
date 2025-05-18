tp_numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
              'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

digito_selec = -1
while digito_selec > 20 or digito_selec < 0:
    digito_selec = int(input("Digite um número entre 0 e 20: "))

print(f'Você digitou o número {tp_numeros[digito_selec]}')
