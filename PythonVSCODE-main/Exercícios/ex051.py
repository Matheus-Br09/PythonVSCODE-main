pri_termo = int(input('Primeiro termo: '))
raz_termo = int(input('Razão: '))
dec_termo = pri_termo + (10-1) * raz_termo
for c in range(pri_termo, dec_termo+1,raz_termo):
    print(f'{c}', end=' → ')
print("FIM")