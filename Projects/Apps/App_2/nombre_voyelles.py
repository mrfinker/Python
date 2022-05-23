def count_voyel(phrases):
    count = 0
    voyel = ["a","e","y","u","i","o","A","E","Y","U","I","O"]
    for char in phrases:
        if char in voyel:
            count = count + 1
    return count

print(count_voyel("Bienvenue a tous"))