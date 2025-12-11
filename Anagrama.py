from collections import Counter
def anagrama(cadena1, cadena2):
    # Limpiamos espacios, convertimos a minúsculas
    cadena1 = cadena1.replace(" ", "").lower()
    cadena2 = cadena2.replace(" ", "").lower()

    # Si no son igual de largos
    if len(cadena1) != len(cadena2):
        return False

    # Contamos caracteres de ambas cadenas
    return Counter(cadena1) == Counter(cadena2)

# True
print(anagrama("Roma", "Amor"))
# True
print(anagrama("Escucha", "CauchES"))
# False
print(anagrama("Hola", "Adios"))