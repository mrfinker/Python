"""
Arguments

Le programme donné définit une fonction printBill(), qui prend un argument de chaîne et génère du texte formaté.
Vous devez prendre l'entrée de l'utilisateur et appeler la fonction en passant l'entrée comme argument.
Vous devez uniquement appeler la fonction, car elle s'occupera de la sortie.
"""

def printBill(text):
    print("======")
    print(text)
    print("======")

a = input()
printBill(a)