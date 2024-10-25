def inverseTexteFonctionnel(texte):
    if texte == "":
        return ""
    else:
        return inverseTexteFonctionnel(texte[1:]) + texte[0]

# Exemple d'utilisation
print(inverseTexteFonctionnel("abcd"))  # Résultat attendu : "dcba"
