#Ejercicio 1: Verificación de número primo con control
#de errores
#Escribe un programa que solicite al usuario un número entero positivo y determine si es
#primo. El programa debe:
#- Validar que el número sea entero y positivo.
#- Lanzar una excepción si el valor no cumple con estas condiciones.
#- Mostrar si el número es primo o no, explicando por qué (por ejemplo, “No es primo
#porque es divisible por 3”).
import math

num=0;
Resultado="no valido"
try:
    num = int(input("Ingresa tu numero: "))
    Resultado = "es primo"
    for i in range(2, num):
        if num % i == 0:
            Resultado = "no es primo, divisible entre " + str(i)
except:
    print("numero no valido")

print(Resultado);

#Ejercicio 2: Conversor de divisas con control de errores
#Crea un programa que convierta una cantidad en euros a otra divisa (USD, GBP o JPY). El
#usuario debe introducir:
#- La cantidad en euros.
#- La divisa destino.
#El programa debe:
#- Validar que la cantidad sea un número positivo.
#- Validar que la divisa esté entre las permitidas.
#- Manejar excepciones si el usuario introduce datos incorrectos.

Cantidad=0.0
Divisa="";
try:
    Cantidad= float(input("Ingresa tu cantidad:"))
    resultado = Cantidad
    Divisa= str(input("Ingresa tu divisa (USD, GBP, JPY):"))
    if Cantidad<0 or Divisa!="USD" and Divisa!="GBP" and Divisa!="JPY":
            print("Divisa o cantidad no valida")
    else:
        match Divisa:
            case "USD":
                resultado = Cantidad * 1.17;
            case "GBP":
                resultado = Cantidad * 0.87;
            case "JPY":
                resultado = Cantidad * 176.05;

except:
    print("numero no valido")
print("resultado= "+ str(resultado))

#Ejercicio 3: Cálculo de raíces reales de una ecuación cuadrática
#Solicita al usuario los coeficientes a, b y c de una ecuación cuadrática de la forma: ax² + bx + c = 0
#El programa debe:
#- Validar que a no sea cero (ya que no sería una ecuación cuadrática).
#- Calcular el discriminante D = b² - 4ac.
#- Lanzar una excepción si no hay raíces reales (es decir, si el discriminante es negativo).
#- Mostrar las raíces reales si existen.

try:
    a=int(input("Coeficiente a: "))
    b=int(input("Coeficiente b: "))
    c=int(input("Coeficiente c: "))
    if a>=0:
        raise ValueError("Coeficiente a invalido")
    D= b**2 -4*a*c
    if D<0:
        raise ValueError("Discriminante invalido")
# Calcular raíces
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)

    # Mostrar resultados
    print(f"Las raíces reales son: x1 = {x1:.2f}, x2 = {x2:.2f}")

except ValueError as e:
    print("Error:", e)

# Ejercicio 4: Simulador de cajero automático
# Simula un cajero automático que permite retirar dinero de una cuenta. El usuario debe introducir:
# - Saldo inicial.
# - Cantidad a retirar.
# El programa debe:
# - Validar que el saldo y la cantidad sean números positivos.
# - Comprobar si hay suficiente saldo.
# - Lanzar una excepción si se intenta retirar más de lo disponible.
# - Mostrar el saldo restante.

try:
    Saldo = float(input("Ingresa tu saldo: "))
    Retiro = float(input("Ingresa tu retiro: "))
    if Saldo>0 and Retiro>0:
        if Retiro > Saldo:
            raise ValueError("Saldo invalido")
        else:
            print("Retirando")
            Saldo-= Retiro
except ValueError as e:
    print("Error:", e)
print("Saldo =", Saldo)

# Ejercicio 5: Calculadora de operaciones con manejo
# múltiple de excepciones
# Crea una calculadora que permita al usuario introducir dos números y una operación (+, -, *,
# /). El programa debe:
# - Validar que los números sean válidos.
# - Manejar la división por cero.
# - Manejar operaciones no reconocidas.
# - Usar try-except con múltiples bloques para capturar distintos errores.

