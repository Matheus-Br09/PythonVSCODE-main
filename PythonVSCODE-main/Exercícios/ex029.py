car_speed = float(input('Velocidade do carro [Km/h]: '))
if car_speed > 80:
    multa_pKm = (car_speed - 80) * 7
    print(f'Você recebeu uma multa de R${multa_pKm: .2f}'.replace('.', ','))
else:
    print(f'Você está dentro do limite de velocidade')