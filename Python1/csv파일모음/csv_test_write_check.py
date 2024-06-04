import csv
fw = open("month_oct.csv", "r", encoding="UTF-8")

new = csv.reader(fw)

for i in new:
    print(i)

fw.close()
