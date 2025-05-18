peso_pessoa = float(input("Digite seu peso: "))
altura_pessoa = float(input("Digite sua altura: "))
imc = peso_pessoa / (altura_pessoa * altura_pessoa)
print(f'Seu IMC é de: {imc:.2f}')
print("Você está: ", end='')
if imc < 18.5:
    print('ABAIXO DO PESO')
if imc >= 18.5 and imc < 24.9:
    print('NORMAL')
if imc >= 25 and imc < 29.9:
    print('SOBREPESO')
if imc >= 30 and imc < 39.9:
    print('OBESIDADE')
if imc >= 40:
    print('OBESIDADE MÓRBIDA')