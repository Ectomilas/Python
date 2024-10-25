################### Fonctions #######################
def algoDijkstraDistances(graphe, depart):
    distances = {depart: 0}
    chemins = {depart: [depart]}
    non_visites = set(graphe.keys())
    while non_visites:
        courant = min(non_visites, key=lambda x: distances.get(x, float('inf')))
        non_visites.remove(courant)
        for voisin, poids in graphe[courant]:
            if voisin in non_visites:
                nouvelle_distance = distances[courant] + poids
                if nouvelle_distance < distances.get(voisin, float('inf')):
                    distances[voisin] = nouvelle_distance
                    chemins[voisin] = chemins[courant] + [voisin]
    return distances, chemins

def plusCourtChemin(graphe, depart, arrive):
    distances, chemins = algoDijkstraDistances(graphe, depart)
    if arrive not in chemins:
        return "Il n'y a pas de chemin de {} à {}".format(depart, arrive)
    chemin = chemins[arrive]
    return ' -> '.join(map(str, chemin))
######################################################

################### Variables #######################
graphe4 = { 1:[(2,6), (3,2), (4,4)],
            2:[(1,6), (4,2)],
            3:[(1,2), (4,1)],
            4:[(1,4), (2,2), (3,1)] }

graphe5 = { 1:[(2,2), (3,6)],
            2:[(1,2), (3,2), (4,9), (5,1)],
            3:[(1,6), (2,2), (4,2)],
            4:[(2,9), (3,3)],
            5:[(2,1)] }
######################################################


################### Affichage #######################
print("Distances du graphe 4 : "algoDijkstraDistances(graphe4, 1)[0])
print("Distances du graphe 5 : "algoDijkstraDistances(graphe5, 1)[0])
print("Graphe 4 : Chemin le plus court de 1 à 4 :", plusCourtChemin(graphe4, 1, 4))
print("Graphe 5 : Chemin le plus court de 1 à 5 :", plusCourtChemin(graphe5, 1, 5))
######################################################
