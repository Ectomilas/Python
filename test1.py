##################################################
# NSI Parcours en Largeur - 09/02/2024           #
# Zidane Salim, TG1                              #
##################################################

################### Fonctions #######################
def parcoursLargeur(arbre, racine):
    file = [racine]
    resultat = []
    while file:
        noeud_actuel = file.pop(0)
        resultat.append(noeud_actuel)
        file += [enfant for enfant in arbre[noeud_actuel]]
    return resultat

def parcoursLargeurV2(graphe, noeud) :
    visite = []
    file = [noeud]
    while file:
        noeud = file.pop(0)
        if noeud not in visite :
            visite.append(noeud)
            if graphe[noeud] :
                file.extend(graphe[noeud])
    return visite

def parcoursLargeurCycle(graphe, noeud):
    visite = []
    file = [(noeud, None)]
    while file:
        noeud, parent = file.pop(0)
        if noeud in visite:
            #print("Il y a un cycle")
            return True
        visite.append(noeud)
        for voisin in graphe[noeud]:
            if voisin != parent:
                file.append((voisin, noeud))
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
print("Parcours en largeur de l'arbre 1 :", parcoursLargeur(arbre1,1))
print("Parcours en largeur de l'arbre 2 :", parcoursLargeur(arbre2,1))

print("Parcours en largeur V2 de l'arbre 1 :", parcoursLargeurV2(arbre1,1))
print("Parcours en largeur V2 de l'arbre 2 :", parcoursLargeurV2(arbre2,1))
print("Parcours en largeur V2 du graphe 1:", parcoursLargeurV2(graphe1,1))
print("Parcours en largeur V2 du graphe 2:", parcoursLargeurV2(graphe2,1))
print("Parcours en largeur V2 du graphe 3 :", parcoursLargeurV2(graphe3,1))

print("Cycle dans l'arbre 1 ? :", parcoursLargeurCycle(arbre1,1))
print("Cycle dans l'arbre 2 ? :", parcoursLargeurCycle(arbre2,1))
print("Cycle dans le graphe 1 ? :", parcoursLargeurCycle(graphe1,1))
print("Cycle dans le graphe 2 ? :", parcoursLargeurCycle(graphe2,1))
print("Cycle dans le graphe 3 ? :", parcoursLargeurCycle(graphe3,1))
######################################################
