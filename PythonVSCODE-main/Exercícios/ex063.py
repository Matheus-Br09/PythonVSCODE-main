print("--"*12)
print(" Sequência de Fibonacci")
print("--"*12)

fibonacci = int(input("Quantos termos você quer mostrar? "))
p1 = 0
p2 = 1

#print(f'{p1} → ', end='')
while fibonacci != 0:
    print(f'{p1} → ', end='')
    p3 = p1 + p2
    p1 = p2
    p2 = p3
    fibonacci -= 1
print('FIM')