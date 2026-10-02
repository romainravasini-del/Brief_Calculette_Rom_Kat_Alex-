import math

#fontions sinus, cosinus et tangeante
def sin(angle, degres=False):
    return math.sin(math.radians(angle) if degres else angle)

def cos(angle, degres=False):
    return math.cos(math.radians(angle) if degres else angle)

def tan(angle, degres=False):
    return math.tan(math.radians(angle) if degres else angle)

#Choix de l'opération
choix = input("Quelle opération faire : 'cos', 'sin', 'tan' ?").strip().lower()

if choix in ['sin', 'cos', 'tan']:
    #On demande à l'utilisateur l'unité et la valeur
    unite = input("Unité : 'd' pour degré, 'r' pour radian (rad par défaut) :").strip().lower()
    degres = unite == 'd'
    angle = float(input("Entrez la valeur de l'angle : "))

    #Affichage du résultat
    print(f"\nRésultat : ")
    if choix == 'sin':
        print(f" sin({angle}) = {sin(angle, degres)}")
    elif choix == 'cos':
        print(f" cos({angle}) = {cos(angle, degres)}")
    elif choix == 'tan':
        try:
            print(f" tan({angle}) = {tan(angle, degres)}")
        except ValueError:
            print(" tan(x) n'existe pas pour cet angle.")
    else:
        print("Opération invalide. Choisir entre sin, cos ou tan.")
else:
    print("Entrée invalide, recommencez.")