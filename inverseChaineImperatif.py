def inverseTexteImperatif(texte):
    inverse = ""
    for char in texte:
        inverse = char + inverse
    return inverse

# Exemple d'utilisation
print(inverseTexteImperatif("abcd"))  # Résultat attendu : "dcba"
