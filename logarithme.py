import math

def logarithme():
    nombre_1 = float(input("Entrez un nombre : "))
    if nombre_1 < 1:
        print("Le nombre doit être supérieur ou égal à 1.")
    else:
        logarithme = round(math.log(nombre_1), 4)
        print(f"Logarithme de {nombre_1} = {logarithme}")
