from soustraction import soustraction
from addition import additionner_nombres
from racine_carree import calculer_racine
from logarithme import logarithme
from division import division
from multiplication import multiplication
from modulo import modulo
from exponentielle import exponentielle
from trigonometrie import gerer_trigonometrie
from unit_conversion import convertir_unite

def afficher_menu():
    print("\n" + "=" * 50)
    print("\t" * 3 + "Kalkulator" + "\t" * 3) 
    print("=" * 50 + "\n")               
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    print("6. Racine carrée")
    print("7. Exponentielle")
    print("8. Logarithme")
    print("9. Conversions d'unités")
    print("10. Trigonométrie")
    print("11. Quitter")

def saisir_nombre(message):
    while True:
        saisie = input(message)
        try:
            ma_variable = float(saisie)
            return ma_variable
        except ValueError:
            print("Votre saisie est invalide, veuillez recommencer.")

while True:
    afficher_menu()
    choix = input("Entrez votre choix (1-11) : ")

    if choix == "11":
        print("Au revoir !")
        break

    elif choix in ["1", "2", "3", "4", "5", "7"]:
        nombre_1 = saisir_nombre("Entrez votre premier nombre : ")
        nombre_2 = saisir_nombre("Entrez le deuxième nombre : ")
        print(f"Super ! Les nombres validés sont {nombre_1} et {nombre_2}")

        if choix == "1":
            resultat = additionner_nombres(nombre_1, nombre_2)
            print(f"Résultat : {resultat}")
        elif choix == "2":
            resultat = soustraction(nombre_1, nombre_2)
            print(f"Résultat : {resultat}")
        elif choix == "3":
            resultat = multiplication(nombre_1, nombre_2)
            print(f"Résultat : {resultat}")
        elif choix == "4":
            resultat = division(nombre_1, nombre_2)
            print(f"Résultat : {resultat}")
        elif choix == "5":
            resultat = modulo(nombre_1, nombre_2)
            print(f"Résultat : {resultat}")
        elif choix == "7":
            resultat = exponentielle(nombre_1, nombre_2)
            print(f"Résultat : {resultat}")
        

    elif choix in ["6", "8", "9"]:
        if choix == "6":
            num = saisir_nombre("Entrez un nombre : ")
            if num < 0:
                print("Erreur : Impossible de calculer la racine d'un nombre négatif.")
            else:
                resultat = calculer_racine(num)
                print(f"Racine de {num} = {resultat}")
                
        elif choix == "8":
            resultat = logarithme() 
            print(f"Résultat : {resultat}")
            
        elif choix == "9":
            num = saisir_nombre("Entrez la valeur à convertir : ")
            dep = input("Entrez l'unité de départ (miles, km, kg, livres) : ").strip().lower()
            arr = input("Entrez l'unité d'arrivée (miles, km, kg, livres) : ").strip().lower()
            resultat = convertir_unite(num, dep, arr)

    elif choix == "10":
        gerer_trigonometrie()
        

    else:
        print("Choix invalide, veuillez recommencer.")