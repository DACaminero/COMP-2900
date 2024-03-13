#Calcular el Area de un triangulo

base = float(input('Entre la base del triangulo: '))
altura = float(input('Entre la altura del triangulo: '))

def area_triangulo(base, altura):
    return((base*altura)/2)

area = area_triangulo(base, altura)

print(f'El area del triangulo es: ', area)