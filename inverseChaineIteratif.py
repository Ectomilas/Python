def inverseTexteIteratif(texte):
    inverse = ""
    for char in texte:
        inverse = char + inverse
    return inverse

# Exemple d'utilisation
print(inverseTexteIteratif("abcd"))  # Résultat attendu : "dcba"
