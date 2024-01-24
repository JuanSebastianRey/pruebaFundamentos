v1 = float(input('Ingrese el voltaje 1:\n'))
v2 = float(input('Ingrese el voltaje 2:\n'))
v3 = float(input('Ingrese el voltaje 3:\n'))
v4 = float(input('Ingrese el voltaje 4:\n'))
v5 = float(input('Ingrese el voltaje 5:\n'))

pr = ((v1+v2+v3+v4+v5)/5)
if pr > 220:
    print('Alto voltaje')

if pr <= 220:
    print('Voltaje correcto')