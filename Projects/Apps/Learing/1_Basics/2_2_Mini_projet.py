### Mini-projet
# Vous devez calculer les points gagnés par une equipe de football
# L'equipe a remporté 18 jeux et a terminé 7 jeux comme match nul
# Une victoire apporte 3 points, tandis qu'un match null apporte 1 point
### Crez un prpogramme pour calculer et produire le total des points gagnés par l'equipe

match_nul = 7
match_gagner = 18
total_match = match_gagner + match_nul

point_gagner = match_gagner * 3
point_egaliter = match_nul * 1

total_point = point_gagner + point_egaliter

print(total_point)