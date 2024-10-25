def inverseTexteFonctionnel(texte):
    if texte == "":
        return ""
    else:
        return inverseTexteFonctionnel(texte[1:]) + texte[0]
      
# Exemple
print(inverseTexteFonctionnel("abcd"))  # Result : "dcba"
