#1
from logging import exception

try:
    edad = input("Introduce tu edad: ")
    if int(edad) > 0:
        edad = int(edad)
        if edad>18:
            print("mayor de edad")
        else:
            print("menor de edad")
except:
    print("numero no valido")
#2
num1=0
num2=0
salida="Ambos son iguales"
try:
    num1 = int(input("Introduce el primer número entero: "))
    num2 = int(input("Introduce el segundo número entero: "))
except:
    print("numero no valido")
if num1 > num2:
    salida="El primer número es mayor."
elif num2 > num1:
    salida="El segundo número es mayor."
print(salida)
#3
nota = input("Introduce tu nota (0-10): ")
salida="Suspenso"
try:
    nota = float(nota)
    if 0 <= nota <= 10:
        if nota < 5:
            print("Suspenso")
        elif nota < 7:
            print("Aprobado")
        elif nota < 9:
            print("Notable")
        else:
            print("Sobresaliente")
    else:
        print("La nota debe estar entre 0 y 10.")
except ValueError:
    print("Debes introducir un número decimal válido.")
#4
try:
    clave = input("Introduce la clave: ")
except:
    print("No se puede introducir la clave.")
if clave == "python123":
    print("Acceso concedido.")
else:
    print("Acceso denegado.")
