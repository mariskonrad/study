# Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius

def convert_to_celsius(f):
    celsius = 5 * ((f - 32) / 9)
    return celsius

def convert_to_fahrenheit(c):
    fahr = (c * 9/5) + 32
    return fahr

a = convert_to_celsius(90)
print(a)

b = convert_to_fahrenheit(35)
print(b)
