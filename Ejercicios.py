# Exercise 1: Write a program which repeatedly reads integers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the integers.
# If the user enters anything other than a integers, detect their mistake using
# try and except and print an error message and skip to the next integers.

try:
    Total= 0
    Count=0
    avg=0
    while True:
        try:
            numero=str(input("Ingresa un numero: "))
            if numero=="done":
                break
            elif numero!="done" and numero.isdigit():
                Count += 1
                print(Count)
                Total += int(numero) #este cast casi me hunde la carrera futbolistica
                print (Total)
        except ValueError:
            print("Invalid argument")
except:
    print(Exception)
avg = Total/Count
print(str(Total)+" "+str(Count)+ " "+str(avg))

# Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints
# out both the maximum and minimum of the numbers instead of the average.
try:
    maximun=0
    minimun=10
    while True:
        try:
            numero=str(input("Ingresa un numero: "))
            if numero=="done":
                break
            elif numero!="done":
                if int(numero)>maximun:
                    maximun=int(numero)
                if int(numero)<minimun:
                    minimun=int(numero)
        except ValueError:
            print("Invalid argument")
except:
    print(Exception)
print(str(minimun)+" "+str(maximun))

#5 numeros y ordenalos

placeholder=10
numeros=int[5,9,2,8,1]
cont=0
while cont<5:
    for numero in numeros:
        if numeros<placeholder:
            placeholder=numero
            cont+1
        else:
            numeros=placeholder
print(numeros);