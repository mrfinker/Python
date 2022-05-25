nums = {1,2,3,4,5,6}
nums = {0,1,2,3} & nums
nums = filter(lambda x:x > 1, nums)
print(len(list(nums))) #La valeur est deux
print()

def power(x,y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)

print(power(2,3))
print()

#Calcule une expression d'une fonction anonyme et l'appellant par le numero 6
a = (lambda x: x*(x+1))(6)
print(a)
print()

#laisser que les valeurs paires dans la liste
nums = [1,2,8,3,7]
res = list(filter(lambda x:x%2==0, nums))
print(res)
print()

def func(**kwargs):
    print(kwargs["zero"])
func(a = 0, zero = 8) #la reponse est : 8
print()

#La veleur clé utiliser pour renvoyer une valeur du generateur : yield