v1 = float(input('Ingrese el voltaje 1:\n'))
v2 = float(input('Ingrese el voltaje 2:\n'))
v3 = float(input('Ingrese el voltaje 3:\n'))

pr = ((v1+v2+v3)/3)
if pr <= 220 and pr >=115:
    print('Alto voltaje')
elif pr < 115:
    print('Voltaje correcto')
elif pr > 220:
    print('PELIGRO')