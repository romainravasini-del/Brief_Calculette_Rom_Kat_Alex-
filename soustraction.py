def soustraction(nombre_1, nombre_2):
    resultat = nombre_1 - nombre_2
    return resultat

texte_1 = input("Entrez le premier nombre : ")
texte_2 = input("Entrez le deuxième nombre : ")

nombre_1 = int(texte_1)
nombre_2 = int(texte_2)
reponse = soustraction(nombre_1, nombre_2)

print(f"Le résultat est : {nombre_1} - {nombre_2} = {reponse}  ")