class Node:
    def __init__(liste, dataval=None):
        liste.dataval = dataval
        liste.valsuivant = None

class listechainee:
    def __init__(liste):
        liste.teteval = None
    def listeaffiche(liste):
        printval = liste.teteval
        while printval is not None:
            print (printval.dataval)
            printval = printval.valsuivant

liste1 = listechainee()
liste1.teteval = Node("lundi")
e2 = Node("mardi")
e3 = Node("mercredi")
# Relier le premier nœud au deuxième nœud
liste1.teteval.valsuivant = e2
# Relier le deuxième nœud au troisième nœud
e2.valsuivant = e3
liste1.listeaffiche()