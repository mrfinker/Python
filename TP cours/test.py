import uuid

from collections import deque

class ArbreBinaire:
    def __init__(self, valeur):
      self.valeur = valeur
      self.enfant_gauche = None
      self.enfant_milieu = None
      self.enfant_droit = None

    def insert_gauche(self, valeur):
      if self.enfant_gauche == None:
         self.enfant_gauche = ArbreBinaire(valeur)
      else:
         new_node = ArbreBinaire(valeur)
         new_node.enfant_gauche = self.enfant_gauche
         self.enfant_gauche = new_node

    def insert_milieu(self, valeur):
      if self.enfant_milieu == None:
         self.enfant_milieu = ArbreBinaire(valeur)
      else:
         new_node = ArbreBinaire(valeur)
         new_node.enfant_milieu = self.enfant_milieu
         self.enfant_milieu = new_node

    def insert_droit(self, valeur):
      if self.enfant_droit == None:
         self.enfant_droit = ArbreBinaire(valeur)
      else:
         new_node = ArbreBinaire(valeur)
         new_node.enfant_droit = self.enfant_droit
         self.enfant_droit = new_node

    def get_valeur(self):
      return self.valeur

    def get_gauche(self):
      return self.enfant_gauche

    def get_milieu(self):
      return self.enfant_milieu

    def get_droit(self):
      return self.enfant_droit

#######fin de la classe########

######début de la construction de l'arbre###########

racine = ArbreBinaire('1')

racine.insert_gauche('2')
racine.insert_milieu('3')
racine.insert_droit('4')

b_node = racine.get_gauche()
b_node.insert_gauche('5')
b_node.insert_milieu('6')
b_node.insert_droit('7')

c_node = racine.get_milieu()
c_node.insert_gauche('8')
c_node.insert_milieu('9')
c_node.insert_droit('10')

d_node = racine.get_droit()
d_node.insert_gauche('11')
d_node.insert_milieu('12')
d_node.insert_droit('13')

######fin de la construction de l'arbre binaire###########

def affiche(T):
   if T != None:
      return (T.get_valeur(),affiche(T.get_gauche()),affiche(T.get_milieu()),affiche(T.get_droit()))
