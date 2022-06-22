for i in range(1, -2, -1):
    print(i, end=" ")
print()
print()


print(0)
for i in range(1, 1):
    print(i)
print()


for i in range(5, 0, -1):
    print(i, end=" ")
print()
print()


sum = 0
for i in range(1, 11):
    if sum > 20:
        break
    sum += i
print(sum)
print()


for i in range(1, 7):
    if i == 4:
        continue
    print(i, end=" ")
print()
print()

num = 0
while num < 7:
    num += 3
    if num == 6:
        continue
    print(num)
print()


for i in range(1,6):
    for j in range(1,6):
        print(i,j)
print()

equation = "160 + 135 = 295"
for symbol in equation:
    if symbol not in "12":
        print(symbol)