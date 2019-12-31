# Decimal to binary conversion without using recursion

li = []

def dec_bin(val):
    print("Binary number without using recursion")
    while val > 1:
        a = val % 2
        li.append(a)
        val = val//2
    li.append(val)
    for i in range(len(li)-1, -1,-1):
        print(li[i],end=" ")


# Decimal to binary conversion using recursion
l = []
def dec_bin_recursion(val):
    if val > 1:
        dec_bin_recursion(val//2)
        a = val % 2
        l.append(a)
    elif val == 1:
        l.append(val)
    else:
        pass

n = int(input("Decimal Number : "))

dec_bin(n)

print("")

dec_bin_recursion(n)

print("Binary number using recursion")
for i in l: 
    print(i,end=" ")

