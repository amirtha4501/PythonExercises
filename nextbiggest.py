# Example code to find the next biggest element of one element in a list
a = []
n = int(input("Enter number of elements in a list : "))

for i in range(0,n):
    ele = int(input("Element: "))
    a.append(ele)

a.sort()

for i in range(0,len(a)-1):
    if a[i+1] > a[i]:
        print("The next of " ,a[i],"is", a[i+1])
        if a[i] > len(a):
            print("The next of " ,a[i+1],"is none")