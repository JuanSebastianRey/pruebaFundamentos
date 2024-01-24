#m/1000=km
m = float(input('Ingrese la distancia a recorrer en metros:\n'))
km = m/1000
if m < 0:
    print('No existe unidades de medida negativas')
else:
    print(km)