import numbers


def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)
print()

#Boucle infinie

# def infinie():
#     while True:
#         yield 7

# for i in infinie():
#     print(i)
# print()


def get_p():
    num = 2
    while True:
        if is_p(num):
            yield num
        num += 1
print()

def nombres(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(nombres(11)))
print()

def mots_creer():
    mots = ""
    for ch in "caleb":
        mots = mots + ch
        yield mots
print(list(mots_creer()))
print()