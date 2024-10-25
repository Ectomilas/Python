class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None

def parcours_largeur(arbre):
    if arbre is None:
        return
    
    file = []  # Utilisation d'une liste pour représenter la file
    file.append(arbre)  # Enfiler la racine
    while file:
        # Défiler le nœud actuel
        noeud_courant = file.pop(0)
        # Traitement du nœud (imprimer ou utiliser la valeur)
        print(noeud_courant.valeur)
        # Enfiler les enfants du nœud actuel (de gauche à droite)
        if noeud_courant.gauche:
            file.append(noeud_courant.gauche)
        if noeud_courant.droit:
            file.append(noeud_courant.droit)



racine = Noeud(5)
racine.gauche = Noeud(8)
racine.droit = Noeud(3)
racine.droit.gauche = Noeud(1)
racine.droit.gauche.gauche = Noeud(2)
racine.droit.gauche.droit = Noeud(6)

parcours_largeur(racine)
