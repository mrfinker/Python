try:
    print(1)
    print(20/0)
    print(2)
except ZeroDivisionError:
    print(3)
finally:
    print(4)
print()

x = 3
try:
    x += "2"
except:
    x += 2
else:
    x += 4
finally:
    print(x)
print()

m = 0
try:
    m += 1
    raise ValueError
except NameError:
    m += 1
except ValueError:
    m += 1
else:
    m += 1
finally:
    m += 1
    print(m)
