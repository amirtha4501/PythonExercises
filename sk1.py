import json

# data = {'name' : 'ammu'}
# res = json.dumps(data)
# print(res)
# print(type(res))
# ser = json.loads(res)
# print(ser)
# print(type(ser))

with open("sk1.json","w") as f:
    data = {
        'name' : 'ammu',
        'age'  : 18,
        'Nature' : 'better'
    }
    json.dump(data, f, indent=4, sort_keys= True)   #, separators=("*","-")
with open("sk1.json","r") as fr:
    print(json.load(fr))