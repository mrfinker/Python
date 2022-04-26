from collections import deque

généaListe = {}
généaListe['1'] = ['2', '3', '4']
généaListe['2'] = ['5', '6', '7']
généaListe['3'] = ['8']
généaListe['4'] = ['9', '10']
généaListe['5'] = ['11', '12', '13']
généaListe['6'] = ['14']
généaListe['7'] = ['15', '16']
généaListe['8'] = ['17']
généaListe['9'] = ['18', '19']
généaListe['10'] = ['20', '21', '22']
généaListe['11'] = []
généaListe['12'] = []
généaListe['13'] = []
généaListe['14'] = []
généaListe['15'] = []
généaListe['16'] = []
généaListe['17'] = []
généaListe['18'] = []
généaListe['19'] = []
généaListe['20'] = []
généaListe['21'] = []
généaListe['22'] = []

paragraphe = 1

if paragraphe == 1:
    
    def parcourLargeur(graph, debut):
        A_visiter = deque()
        A_visiter.appendleft(debut)
        dejavu = [debut]
        while A_visiter:
            noeud = A_visiter.pop()
            print("En cours de visite :", noeud)
            for voisin in graph [noeud]:
                if voisin not in dejavu:
                    A_visiter.appendleft(voisin)
                    
    print("Parcours en largeur")
    print("------------------------------")
    parcourLargeur(généaListe, '1')
    print("*"*25)