def sup_double(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique

nombres = [22,11,3,1,4,5,5,2,2,11,66,89]
print(sup_double(nombres))