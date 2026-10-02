import math

def racine_caree():
    nombre_1 = float(input("Entrez un nombre : "))
    if nombre_1 < 0:
        print("Le nombre doit être supérieur ou égal à 0.")
    else:
        racine_carre = round(math.sqrt(nombre_1), 4)
        print(f"Racine de {nombre_1} = {racine_carre}")
