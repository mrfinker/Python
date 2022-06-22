import math as m

width = float(input("Veuillez entrer la valeur du width : "))
height = float(input("Veuillez entrer la valeur du height : "))

perimetre = 2*(width+height)
area = width*height
diagonal = m.sqrt(m.pow(width, 2) + m.pow(height, 2))

print(perimetre)
print(area)
print(diagonal)