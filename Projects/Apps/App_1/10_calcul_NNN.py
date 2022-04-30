#Programme python qui accepte un entier (n) et calcule la valeur de n + nn + nnn

a = int(input("Entrer un entier : "))
n1 = int("%s" %a)
n2 = int("%s%s" %(a,a))
n3 = int("%s%s%s" %(a,a,a))

print(n1+n2+n3)
print(n1*n3)