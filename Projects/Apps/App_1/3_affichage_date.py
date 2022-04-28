#Programme python qui affiche la date et le temps actuel

import datetime
from tkinter import Y
now = datetime.datetime.now()
print("Date et l'heure actuelle : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))