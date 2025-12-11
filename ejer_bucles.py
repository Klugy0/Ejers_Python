import random
#1
try:
    while(True):
        operacion = input("Ingresa una operacion: ")
        if operacion== "salir":
            print("Saliendo...")
            break
        op1= int(input("Ingresa un numero: "))
        op2= int(input("Ingresa un numero: "))
        result = 0
        def sacarResultado(operacion, op1, op2):
            result = 0
            match operacion:
                case "+":
                    result = op1 + op2
                case "-":
                    result = op1 - op2
                case "*":
                    result = op1 * op2
                case "/":
                    result = op1 / op2
                case _:
                    print("Operacion no valida")

            return result
        result=sacarResultado(operacion, op1, op2)
except ValueError:
    print("El numero ingresado no es valido")
except ArithmeticError:
    print("El numero ingresado no es valido")

print("resultado:" + str(result))
#2
try:
    numero= int(input("Ingresa un numero: "))
    def tablamult(numero):
        for x in range(1,11):
            print(str(numero) +" * "+str(x) +": " +str(numero*x))
    tablamult(numero)
except ValueError:
    print("El numero ingresado no es valido")

#3
numeroAl= random.randint(1,101)
def adivinar(numeroAl):
    acierto = False
    while acierto == False:
        numero = int(input("Ingresa un numero: "))
        if numero==numeroAl:
            acierto=True
            print("El numero ingresado es correcto")
        elif numero>numeroAl:
            print("el numero es menor")
        elif numero<numeroAl:
            print("el numero es mayor")
adivinar( numeroAl)
#5
numero= int(input("Ingresa un numero: "))
listaPrimos= ""
for i in range(1, numero):
    primo = True
    for j in range(2, i):
        if i % j == 0:
            primo = False
    if primo==True:
        listaPrimos +=str(i)+", "
print(listaPrimos)
#6
notas = [1,8,3,3,5,9,1,8,9,10]
contador=0
notaMedia=0
notaBaja=100
notaAlta=0
for x in range (len(notas)):
    if notas[x]>=5:
        contador+=1
    notaMedia+=notas[x]
    if notas[x]< notaBaja:
        notaBaja=notas[x]
    if  notas[x]>notaAlta:
        notaAlta=notas[x]
print("numero aprobados: "+str(contador))
print("media de notas: " + str(notaMedia/len(notas)))
print("nota mas alta:"+ str(notaAlta))
print("nota mas baja:"+ str(notaBaja))
