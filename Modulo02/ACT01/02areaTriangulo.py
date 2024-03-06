#Calcular el Area de un triangulo


base = float(print('Entre la base del triangulo: '))
altura = float(print('Entre la altura del triangulo: '))

def area_triangulo(base, altura):
    return((base * altura)/2)

print(f'El area del triangulo es: {area_triangulo}')