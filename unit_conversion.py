def convertir_unite(valeur, unite_depart, unite_arrivee):
    if unite_depart == "miles" and unite_arrivee == "km":
        return valeur * 1.60934
    if unite_depart == "km" and unite_arrivee == "miles":
        return valeur * 0.621371
    if unite_depart == "kg" and unite_arrivee == "livres" :
        return valeur * 2.20462
    if unite_depart == "livres" and unite_arrivee == "kg":
        return valeur / 2.20462
    else:
        return "Conversion non disponible"
