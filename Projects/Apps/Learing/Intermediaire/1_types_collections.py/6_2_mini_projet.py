"""
Ensembles


Vous travaillez sur une plateforme de recrutement, qui doit faire correspondre les postes disponibles et les candidats en fonction de leurs compétences.
Les compétences requises pour le poste et les compétences du candidat sont stockées dans des ensembles.
Terminez le programme pour produire la compétence correspondante.
Vous pouvez utiliser l'opérateur d'intersection pour obtenir les valeurs présentes dans les deux ensembles.
"""

skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}
print(list(skills & job_skills)[0])