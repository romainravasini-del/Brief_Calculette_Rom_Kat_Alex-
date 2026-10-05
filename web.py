import streamlit as st
import math
from soustraction import soustraction
from addition import additionner_nombres
from racine_carree import calculer_racine
from logarithme import logarithme
from division import division
from multiplication import multiplication
from modulo import modulo
from exponentielle import exponentielle
from unit_conversion import convertir_unite


st.title("🧮 Notre Super Calculatrice Graphique")

nombre_1 = 0.0
nombre_2 = 0.0

choix = st.selectbox(
    "Choisissez une opération :",
    [
        "Addition", 
        "Soustraction", 
        "Multiplication", 
        "Division", 
        "Modulo", 
        "Racine carrée", 
        "Exponentielle", 
        "Logarithme",
        "Conversions d'unités",
        "Trigonométrie"
    ]
)

if choix in ["Racine carrée", "Logarithme"]:
    nombre_1 = st.number_input("Entrez le nombre :", value=1.0 if choix == "Logarithme" else 0.0)

elif choix == "Conversions d'unités":
    valeur_conv = st.number_input("Valeur à convertir :", value=1.0)
    unite_dep = st.selectbox("Unité de départ :", ["miles", "km", "kg", "livres"])
    unite_arr = st.selectbox("Unité d'arrivée :", ["miles", "km", "kg", "livres"])

elif choix == "Trigonométrie":
    type_trigo = st.selectbox("Opération souhaitée :", ["sin", "cos", "tan"])
    unite_angle = st.radio("Unité de l'angle :", ["Degrés", "Radians"])
    angle_val = st.number_input("Entrez la valeur de l'angle :", value=0.0)

else:
    nombre_1 = st.number_input("Entrez votre premier nombre :", value=0.0)
    nombre_2 = st.number_input("Entrez le deuxième nombre :", value=0.0)

if st.button("Calculer 🚀"):
    
    if choix == "Addition":
        resultat = additionner_nombres(nombre_1, nombre_2)
        st.success(f"Résultat : {resultat}")
        
    elif choix == "Soustraction":
        resultat = soustraction(nombre_1, nombre_2)
        st.success(f"Résultat : {resultat}")
        
    elif choix == "Multiplication":
        resultat = multiplication(nombre_1, nombre_2)
        st.success(f"Résultat : {resultat}")
        
    elif choix == "Division":
        if nombre_2 == 0:
            st.error("Erreur : Division par zéro impossible !")
        else:
            resultat = division(nombre_1, nombre_2)
            st.success(f"Résultat : {resultat}")
        
    elif choix == "Modulo":
        if nombre_2 == 0:
            st.error("Erreur : Modulo par zéro impossible !")
        else:
            resultat = modulo(nombre_1, nombre_2)
            st.success(f"Résultat : {resultat}")
            
    elif choix == "Exponentielle":
        resultat = exponentielle(nombre_1, nombre_2)
        st.success(f"Résultat : {resultat}")
        
    elif choix == "Logarithme":

        resultat = logarithme(nombre_1)
        if isinstance(resultat, str):
            st.error(resultat)
        else:
            st.success(f"Résultat : {resultat}")
        
    elif choix == "Racine carrée":
        if nombre_1 < 0:
            st.error("Erreur : Impossible de calculer la racine d'un nombre négatif.")
        else:
            resultat = calculer_racine(nombre_1)
            st.success(f"Résultat : {resultat}")

    elif choix == "Conversions d'unités":
        resultat = convertir_unite(valeur_conv, unite_dep, unite_arr)
        if isinstance(resultat, str):
            st.error(resultat)
        else:
            st.success(f"Résultat : {valeur_conv} {unite_dep} = {resultat:.2f} {unite_arr}")

    elif choix == "Trigonométrie":
        angle_rad = math.radians(angle_val) if unite_angle == "Degrés" else angle_val
        
        if type_trigo == "sin":
            st.success(f"sin({angle_val}) = {math.sin(angle_rad):.4f}")
        elif type_trigo == "cos":
            st.success(f"cos({angle_val}) = {math.cos(angle_rad):.4f}")
        elif type_trigo == "tan":
            if unite_angle == "Degrés" and angle_val % 180 == 90:
                st.error("Erreur : La tangente n'existe pas pour cet angle.")
            else:
                st.success(f"tan({angle_val}) = {math.tan(angle_rad):.4f}")
