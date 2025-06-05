def eh_par(num):
  if num % 2 == 0:
      return True
  else:
      return False
n = int(input("Digite um número inteiro positivo: "))
pares = []
for num in range(1, n + 1):
    if eh_par(num):
        pares.append(num)
print(f"Números pares de 1 até {n} são: {pares}")