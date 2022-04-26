
# CONCEPTION D'UN ARBRE GENERALISE, PUIS LE BINARISE
"""Dans un premier temps le programme doit constuire un arbre généraliser, 
puis vient en suite l'étape de la binarisation, après celle on doit etre en mésure de supprimer un noeud
et nous finirons pas l'épate du liste chainee """

import anytree

def config_id(id):
    return id.strip().replace(" ","")

(_AJOUT, _SUPPR, _INSERT) = range(3)
(_ROOT, _PRE, _LARGEUR) = range(3) 

class Noeud:
    def __init__(self, nom, identifier=None, exp=True):

        self.__identifier = (str(uuid.uuid1()) if identifier is None else
        config_id(str(identifier)))

        self.nom = nom          # Nom pour indiquer le nom de la variable
        self.exp = exp          # exp pour indiquer la relation avec les restes des noeeuds
        self.__dpointer = None   # pointeur du début de la liste
        self.__fpointer = []     # pointeur de fin de liste

    @property
    def identifier(self):
        return self.__identifier

    @property
    def dpointer(self):
        return self.__dpointer

    @dpointer.setter
    def dpointer(self, value):
        if value is not None:
            self.__dpointer = config_id(value)

    @property
    def fpointer(self):
        return self.__fpointer
    
    def update_fpointer(self, identifier, mode=_AJOUT):
        if mode is _AJOUT:
            self.__fpointer.append(config_id(identifier)) # Ajouter un noeud dans la liste des noeuds finals
        elif mode is _SUPPR:
            self.__fpointer.remove(config_id(identifier)) # Supprimer un noeud dans la liste des noeuds finals
        elif mode is _INSERT:
            self.__fpointer = [config_id(identifier)]  # Inserer un noeud dans la liste des noeuds finals


class Arbre:
    def __init__(self):
        self.noeuds=[]

    #configuration des noeuds
    def get_index(self, position):
        for index, noeud in enumerate(self.noeuds):
            if noeud.identifier == position:
                break
        return index

    def cree_noeud(self, nom, identifier=None, parent=None):
        noeud = Noeud(nom, identifier)
        self.noeuds.append(noeud)
        self.__update_fpointer(parent, noeud.identifier, _AJOUT)
        noeud.dpointer = parent
        return noeud

    def supprimer_noeud(self, nom, identifier=None, parent=None):
        noeud = Noeud(nom, identifier)
        self.noeuds.remove(noeud)
        self.__update_fpointer(parent, noeud.identifier, _SUPPR)
        noeud.dpointer = parent
        return noeud

    def afficher(self, position, niveau=_ROOT):
        feuille = self[position].fpointer
        if niveau == _ROOT:
            print("{0}[{1}]".format(self[position].nom, self[position].identifier))
        else:
            print("\t"*niveau,"{0}[{1}]".format(self[position].nom, self[position].identifier))
        if self[position].exp:
            niveau +=1
            for element in feuille:
                self.afficher(element, niveau) #un appel recursif pour un noeud qui est parent à son tours

    def binariser(self, position, niveau=_ROOT):
        feuille = self[position].fpointer
        if niveau == _ROOT:
            print("{0}[{1}]".format(self[position].nom, self[position].identifier))
        else:
            print("\t"*niveau,"{0}[{1}]".format(self[position].nom, self[position].identifier))
        if self[position].exp:
            for e in feuille:
                niveau +=1
                self.binariser(e, niveau)

    def in_ordre(self, position, niveau=_ROOT):
        parcour=self[position].fpointer
        if self[position].exp:
            for p in parcour:
                self.in_ordre(p, niveau)
        if niveau == _ROOT:
            print(self[position].identifier)
        else:
            print(self[position].identifier)
        

    def parcour_arbre(self, position, mode=_PRE):
        parcour = self[position].fpointer
        while parcour:
            yield parcour[0] # return un géneratuer des nos noeuds en fonction du parcour choisit
            element = self[parcour[0]].fpointer
            if mode is _PRE:
                parcour = element + parcour[1:]
            elif mode is _LARGEUR:
                parcour = parcour[1:]+ element

    def est_branche(self, position):
        return self[position].fpointer

    def __update_fpointer(self, position, identifier, mode):
        if position is None:
            return
        else:
            self[position].update_fpointer(identifier, mode)
    
    def __update_dpointer(self, position, identifier):
        self[position].dpointer = identifier

    def __getitem__(self, key):
        return self.noeuds[self.get_index(key)]

    def __setitem__(self, key, item):
        self.noeuds[self.get_index(key)]= item

    def __len__(self):
        return len(self.noeuds)

    def __contrainte__(self, identifier):
        return[noeud.identifier for noeud in self.noeuds if noeud.identifier is identifier]

if __name__=="__main__":
    
    arbre = Arbre()
    arbre.cree_noeud("1", "a")
    arbre.cree_noeud("2", "b", parent="a")
    arbre.cree_noeud("3", "c", parent="a")
    arbre.cree_noeud("4", "d", parent="a")
    arbre.cree_noeud("5", "e", parent="b")
    arbre.cree_noeud("6", "f", parent="b")
    arbre.cree_noeud("7", "g", parent="b")
    arbre.cree_noeud("8", "h", parent="c")
    arbre.cree_noeud("9", "i", parent="c")
    arbre.cree_noeud("10", "t", parent="c")

    #arbre.supprimer_noeud("8", "h", parent="c")
    
    print("-"*30+" ARBRE GENERALISE "+"-"*30)
    arbre.afficher("a")
    print("\n")
    print("-"*33+" ARBRE BINARISE "+"-"*33)
    arbre.binariser("a")
    print("\n")
    print("-"*33+" PARCOURS "+"-"*33)
    arbre.in_ordre("a")
    #for noeud in arbre.parcour_arbre("a", mode=_PRE):
    #    print(noeud)
    print("\n")
    print("-"*80)
