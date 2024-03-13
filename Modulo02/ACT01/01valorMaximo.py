#Calcular el maximo de dos numero

a = float(input("Ingrese un numero: "))
b = float(input("Ingrese otro numero: "))

def maximo(a, b):
    if a > b:
        return a
    else:
        return b
    
num_max = maximo(a, b)

print("El maximo entre los dos numero: ", num_max)