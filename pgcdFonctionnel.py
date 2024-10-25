def pgcdFonctionnel(n1, n2):
    if n2 == 0:
        return n1
    else:
        return pgcd_func(n2, n1 % n2)

# Exemple d'utilisation
print(pgcdFonctionn(20, 16))  # Résultat attendu : 4
