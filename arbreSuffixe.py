class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None

def parcours_suffixe(arbre):
    if arbre is not None:
        parcours_suffixe(arbre.gauche)
        parcours_suffixe(arbre.droit)
        print(arbre.valeur)


racine = Noeud(5)
racine.gauche = Noeud(8)
racine.droit = Noeud(3)
racine.droit.gauche = Noeud(1)
racine.droit.gauche.gauche = Noeud(2)
racine.droit.gauche.droit = Noeud(6)

parcours_suffixe(racine)
