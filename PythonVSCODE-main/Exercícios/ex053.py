frase = str(input("Digite uma frase para detectar se é PALINDROMO: ")).strip().replace(' ', '').upper()
inverso = ''
for letra in range(len(frase) -1, -1 , -1):
    inverso += frase[letra]

if frase == inverso:
    print('É UM palíndromo')
else:
    print('NÃO É um palíndromo')