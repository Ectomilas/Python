class Liste:
    def __init__(self, nom, suivant=None):
        self.nom = nom
        self.suivant = suivant
    
    def affiche(self):
        if self.suivant!=None : self.suivant.affiche()
        print(self.nom)

L1 = Liste("eleve1", None)
L2 = Liste("eleve2", L1)
L3 = Liste("eleve3", L2)
L4 = Liste("eleve4", L3)

L4.affiche()

#def affiche(self):
    #if self.suivant!=None : self.suivant.affiche()
    #print(nom)
