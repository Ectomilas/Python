class Noeud :
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def parcoursInfixe(a):
    if a.left :
        parcoursInfixe(a.left)
    print(a.value,end=',')
    if a.right :
        parcoursInfixe(a.right)

def parcoursPrefixe(a):
    print(a.value,end=',')
    if a.left :
        parcoursInfixe(a.left)
    if a.right :
        parcoursInfixe(a.right)

def parcoursSuffixe(a):
    if a.left :
        parcoursInfixe(a.left)
    if a.right :
        parcoursInfixe(a.right)
    print(a.value,end=',')

def parcoursLargeur(a):
    file = [a]  
    while file:
        Noeud = file.pop(0)
        print(Noeud.value, end=",")
        if Noeud.left:
            file.append(Noeud.left)
        if Noeud.right:
            file.append(Noeud.right)

Arbre1 = Noeud(5, Noeud(8), Noeud(3, Noeud(1, Noeud(2), Noeud(6)), None))

print("Parcours infixe :")
parcoursInfixe(Arbre1)
print("\n\nParcours prefixe :")
parcoursPrefixe(Arbre1)
print("\n\nParcours suffixe :")
parcoursSuffixe(Arbre1)
print("\n\nParcours en largeur :")
parcoursLargeur(Arbre1)
