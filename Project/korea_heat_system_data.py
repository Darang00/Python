import csv
import numpy as np

f = open("korea_heat_system_operation_plan_20230926.csv", "r", encoding="cp949")

lines = csv.reader(f)

head = next(lines)
print(head) #['시나리오 ID', '계획년도', '계획일자', '열생산량', '전기생산량']


for i in lines:
    print(i)

file.close()
    
