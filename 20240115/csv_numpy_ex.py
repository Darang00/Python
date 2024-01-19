import numpy as np
import csv

f = open("school_2019.csv", "r", encoding="utf-8")

x = csv.reader(f)

head = next(x)
print(head)

data=[]
for i in x:
    if '김해시' in i[0] :
        #print(i)
        data.append(i)

print(data)

#numpy 배열에 학급수, 학생수, 교사수만 저장
#arr_numpy  = np.zeros((4, 2)) #첫 번째 변수가 행 개수, 두 번째 변수가 열 개수
print("row_num", len(data)) #58 행 개수
print("column_num", len(data[0])) #5 열 개수
arr_numpy = np.zeros(len(data), len(data[0]))

#print(arr_numpy)





f.close()
