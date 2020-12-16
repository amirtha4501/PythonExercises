import json

n = str(input("Enter name : "))
p1 = str(input("Enter place1 : "))
p2 = str(input("Enter place2 : "))
id = int(input("Id : "))

# with open("sk4.json","w") as f:
# #    if id != data[]
#     b = json.dump(data,f)

a = dict()
with open("sk4.json","r+") as f:
    data = json.load(f)
    data = {
        "name" : n,
        "place" : [p1, p2] 
        }
    a[id] = data
    data.update(a)
