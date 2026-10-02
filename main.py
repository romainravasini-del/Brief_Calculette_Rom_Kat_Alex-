from soustraction import soustraction
from addition import additionner_nombres
from racine_carree import calculer_racine
from logarithme import logarithme
from division import division
from multiplication import multiplication
from modulo import modulo
from exponentielle import exponentielle

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