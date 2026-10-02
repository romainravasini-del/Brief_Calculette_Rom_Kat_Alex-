from importlib import import_module #ta multiplication,division Katerina
from soustraction import soustraction
from addition import additionner_nombres
from racine_carree import calculer_racine
division = import_module(
    "Kat_ multiplication.division"
).division
modulo = import_module(
    "Kat_ multiplication.modulo"
).modulo
multiplication = import_module(
    "Kat_ multiplication.multiplication"
).multiplication
exponentielle = import_module(
    "Kat_multiplication.exponentielle"
).exponentielle

def saisir_nombre(message):
    while True:
        saisie = input(message)
        try:
            ma_variable=float(saisie)
            return ma_variable
        except ValueError:
            print("Votre saisie est invalide, veuillez recommencer")
            continue
        
nombre_1 = saisir_nombre("Entrez votre premier nombre : ")
nombre_2 = saisir_nombre("Entrez le deuxième nombre : ")
print(f"Super ! Les nombres validés sont {nombre_1} et {nombre_2}")

num = saisir_nombre("Entrez un nombre : ")

if num < 0:
    print("Erreur : Impossible de calculer la racine d'un nombre négatif.")
else:
    resultat = calculer_racine(num)
    print(f"Racine de {num} = {resultat}")