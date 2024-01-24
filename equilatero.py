b = float(input('Ingrese la base del triangulo:\n'))
a = float(input('Ingrese la altura del triangulo:\n'))
ar = (b*a)/2

if ar > 1000:
    print('DATOS NO VALIDOS')
else:
    print(f'El área del triangulo es:\n{ar}')