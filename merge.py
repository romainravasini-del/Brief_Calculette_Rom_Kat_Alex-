#import
#import
#import
#import
#import
#import
def saisir_nombre(message):
    while True:
        saisie = input(message)
        try:
            ma_variable=float(saisie)
            return ma_variable
        except ValueError:
            print("Votre saisie est invalide, veuillez recommencer")
            return input("Nouvelle saisie")
nombre_1 = saisir_nombre("Entrez votre premier nombre : ")
nombre_2 = saisir_nombre("Entrez le deuxième nombre : ")
print(f"Super ! Les nombres validés sont {nombre_1} et {nombre_2}")