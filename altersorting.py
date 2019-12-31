import itertools

a = []
n = int(input("Enter numeber of elements: "))

for i in range(0, n):
    ele = int(input("Element: "))
    a.append(ele)

a.sort()
b = a.copy()
b.sort(reverse=True)

# Using zip we can access multiple lists simultaneously
for (i, j) in zip(a, b):
    if i == j:
        print(i, end=" ")
        break
    if i == j+1:
        break
    print(j, i, end=" ")