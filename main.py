from soustraction import soustraction
from addition import additionner_nombres
from racine_carree import calculer_racine
from logarithme import logarithme
from division import division
from multiplication import multiplication
from modulo import modulo
from exponentielle import exponentielle

def afficher_menu():
<<<<<<< HEAD
    print("\n" , "=" * 50)
    print("      CALCULATRICE     ")
    print("=" * 50)
=======
    print("\n" + "=" * 50)
    print("\t" * 3 + "Kalkulator" + "\t" * 3) 
    print("=" * 50 + "\n")               
>>>>>>> feature/trigonometrie
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
<<<<<<< HEAD
    print("5. Modulo (Reste)")
    print("6. Logarithme")
    print("7. Racine carrée")
    print("8. Exponentielle")
    print("9. Trigonométrie")
    print("10. Conversions")
    print("11. Quitter")
    print("=" * 50)
    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")
    
        if choix == "1": 
            nombre_1 = saisir_nombre("Entrez votre premier nombre : ")
            nombre_2 = saisir_nombre("Entrez le deuxième nombre : ")

        elif choix == "7":
            num = saisir_nombre("Entrez un nombre : ")
            if num < 0:
                print("Erreur : Impossible de calculer la racine d'un nombre négatif.")
        else:
            resultat = calculer_racine(num)
            print(f"Racine de {num} = {resultat}")
=======
    print("5. Modulo")
    print("6. Racine carrée")
    print("7. Exponentielle")
    print("8. Logarithme")
    print("9. Conversions d'unités")
    print("10. Trigonométie")
    print("11. Quitter")
>>>>>>> feature/trigonometrie

def saisir_nombre(message):
    while True:
        saisie = input(message)
        try:
            ma_variable=float(saisie)
            return ma_variable
        except ValueError:
            print("Votre saisie est invalide, veuillez recommencer")
            continue
        
while True:
    afficher_menu()
    choix = input("Entrez votre choix (1-11) : ")

<<<<<<< HEAD
num = saisir_nombre("Entrez un nombre : ")
=======
    if choix == "11":
        print("Au revoir !")
        break

    elif choix in ["1", "2", "3", "4", "5", "7", "8"]:
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
        elif choix == "8":
            resultat = logarithme(nombre_1, nombre_2)
            print(f"Résultat : {resultat}")
        elif choix == ["6","9"]:
            num = saisir_nombre("Entrez un nombre : ")
            if num < 0:
                print("Erreur : Impossible de calculer la racine ou l'unité d'un nombre négatif.")
        else:
            resultat = calculer_racine(num)
            print(f"Racine de {num} = {resultat}")

    else:
        print("Choix invalide, veuillez recommencer.")
>>>>>>> feature/trigonometrie
