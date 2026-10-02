from importlib import import_module #ta multiplication,division Katerina
from soustraction import soustraction
from addition import additionner_nombres
from addition import racine_carree
division = import_module(
    "Kat_ multiplication.multiplication"
).division
modulo = import_module(
    "Kat_ multiplication.multiplication"
).modulo
multiplication = import_module(
    "Kat_ multiplication.multiplication"
).multiplication

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