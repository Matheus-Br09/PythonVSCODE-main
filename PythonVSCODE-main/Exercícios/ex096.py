def area(largura=0, comprimento=0):
    area = largura * comprimento
    print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é de {area}m².')


print("Controle de terrenos")
print('--'*10)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
area(a, b)