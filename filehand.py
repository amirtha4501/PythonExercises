import json, csv

with open("filehand.json") as f:
    data = json.load(f)

    for i in data:
        a = i['name']
        tot = i['tamil'] + i['english'] + i['maths'] + i['science'] + i['social']
        avg = tot / 5

        ans = {
            "total" : tot,
            "average" : avg
        }
        i["total"] = ans["total"]
        i["average"] = ans["average"]

header = ["name", "student_id", "tamil", "english", "maths", "science", "social","total","average"]

fr = open("filehand.csv","w")  
s = csv.DictWriter(fr, delimiter="\t" , fieldnames=header)
s.writeheader()
s.writerows(data)

with open("filehand.json") as f:
    tam_tot = 0
    eng_tot = 0
    mat_tot = 0
    sci_tot = 0
    soc_tot = 0

    data = json.load(f)
    
    for dic in data:
        tam_tot = tam_tot + dic['tamil']
        eng_tot = eng_tot + dic['english']
        mat_tot = mat_tot + dic['maths']
        sci_tot = sci_tot + dic['science']
        soc_tot = soc_tot + dic['social']

    tam_avg = tam_tot / len(data)
    eng_avg = eng_tot / len(data)
    mat_avg = mat_tot / len(data)
    sci_avg = sci_tot / len(data)
    soc_avg = soc_tot / len(data)
    
    
    print(tam_avg)
    print(eng_avg)
    print(mat_avg)
    print(sci_avg)
    print(soc_avg)







