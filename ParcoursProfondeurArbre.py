################### Fonctions #######################
def parcoursProfondeur(graphe, sommet, marques=None):
    if marques is None:
        marques = []
    marques.append(sommet)
    for voisin in graphe[sommet]:
        if voisin not in marques:
            parcoursProfondeur(graphe, voisin, marques)
    return marques

def parcoursProfondeurCycle(graphe, sommet, marques=None, parent=None):
    if marques is None:
        marques = []
    marques.append(sommet)
    for voisin in graphe[sommet]:
        if voisin not in marques:
            if parcoursProfondeurCycle(graphe, voisin, marques, sommet):
                return True
        elif voisin != parent:
            #print("Il y a un cycle")
            return True
    return False
######################################################


################### Variables #######################
arbre1 = {1:[2,3],2:[4],3:[5],4:[],5:[]}
arbre2 = {1:[2,3],2:[4,5],3:[6,7],4:[],5:[],6:[],7:[]}
graphe1 = {1:[2,3,4],2:[1,3],3:[2,3,4],4:[1,3]}
graphe2 = {1:[2,3,4],2:[1,5,6,7],3:[1],4:[1,7],5:[2,6],6:[2,5],7:[2,4]}
graphe3 = {1:[2,3,4],2:[1,3],3:[1,2,5],4:[1,6],5:[3,6],6:[4,5]}
######################################################


################### Affichage #######################
print("Parcours en profondeur de l'arbre 1 : ", parcoursProfondeur(arbre1,1))
print("Parcours en profondeur de l'arbre 2 : ", parcoursProfondeur(arbre2,1))
print("Parcours en profondeur du graphe 1 : ", parcoursProfondeur(graphe1,1))
print("Parcours en profondeur du graphe 2 : ", parcoursProfondeur(graphe2,1))
print("Parcours en profondeur du graphe 3 : ", parcoursProfondeur(graphe3,1))
print("Parcours en profondeur du graphe 3 : ", parcoursProfondeurCycle(graphe3,1))
######################################################
