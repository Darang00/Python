import csv

f = open("pharm_2019_mod.csv", "r", encoding="utf-8")

lines = csv.reader(f)

for i in lines:
    print(i)
    
f.close()
