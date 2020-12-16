import csv

# f = open("sk2.csv","w", newline="")
# data = [["India","America"], ["is","was"], ["not","my"], ["country","state"]]
# s = csv.writer(f, delimiter="\t")
# s.writerows(data)

# f = open("sk2.csv","w", newline="")
# data = {
#     'name' : "ammu"
# }
# d = csv.DictWriter(f,data.keys())
# d.writeheader()
# d.writerow(data)


f = open("sk2.csv","r", newline="")
# data = {
#     'name' : "ammu"
# }
d = csv.DictReader(f)
s = csv.reader(f)
# print(s)
for i in d:
    print(i)
# d.r(data)
