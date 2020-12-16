import json, csv

with open('sk3.json','r+') as f:
    a = json.load(f)
    # print(a)

f = open('sk3.csv','r+')
data = a
# d = csv.writer(f, delimiter="\t") # 
s = csv.DictWriter(f,fieldnames=["name", "place", "nature"])
s.writeheader()
s.writerows(data)


fc = open("sk3.csv","r")
read = csv.DictReader(fc)
print(read)

writ = json.dumps([row for row in read])
print(writ)  

with open('sk3_3.json','w') as fj:
    fj.write(writ)
