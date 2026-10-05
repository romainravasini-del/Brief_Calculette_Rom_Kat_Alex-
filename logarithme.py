import math 
def logarithme(nombre_1):

    if nombre_1 < 1:
        return "Erreur : Le nombre doit être supérieur ou égal à 1."
    else:
        resultat_log = round(math.log(nombre_1), 4)
        return resultat_log