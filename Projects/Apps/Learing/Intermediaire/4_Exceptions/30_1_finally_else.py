try:
    print("Bonjour")
    print(1/0)
except ZeroDivisionError:
    print("Division avec zero")
finally:
    print("le code s'executera quoi qu'il arrive")
print()

try:
    print(1)
except:
    print(2)
finally:
    print(3)
print()

try:
    print(1)
except ZeroDivisionError:
    print(1)
else:
    print(3)
print()

try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)
print()

try:
    print(1)
    print(1 + "1" == 2)
    print(2)
except TypeError:
    print(3)
else:
    print(4)