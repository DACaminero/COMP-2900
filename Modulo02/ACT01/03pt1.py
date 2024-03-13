#convertir una temperatura de fahrenheit a celsius

fahrenheit = float(input("Ingrese la temperatura en Fharenheit: "))

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

celsius = fahrenheit_a_celsius(fahrenheit)

print("The Temperatura en Celsius es: ", celsius)