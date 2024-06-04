'''
1. 하이스쿨_2019.csv 파일을 불러온 후 2차원 리스트 저장하고 출력

2. 1번에서 저장된 2차원 리스트 데이터 중에서 숫자 데이터에 해당하는 6개의 열 데이터를 배열에 저장


1학년 학급수 1학년 학생수 2학년 학급수 2학년 학생수 3학년 학급수 3학년 학생수

[
[데이터...]
[데이터...]
]

3. 전국의 고등학교에 대해 각 학교의 총 학생수 (1, 2, 3학년 학생 수의 합 )을 구한 후
마지막 열에 삽입 (np.insert(배열이름, 인덱스, 데이터, axis=축기준)

4. 전국 고등학교에 대해 각 학년별 총 학생수를 구하고 막대 그래프로 시각화한다.

'''

import numpy as np
import csv
import matplotlib.pyplot as plt
from matplotlib import rc

f = open("high_school_2019.csv", "r", encoding="utf-8")

x = csv.reader(f)

head = next(x)
#print(head)
#['지역', ' 학교명', ' 1학년 학급수', ' 1학년 학생수', ' 2학년 학급수', ' 2학년 학생수', ' 3학년 학급수', ' 3학년 학생수']

#1.
data=[]
for i in x:
    data.append(i[:])

#print(data)

#2.
arr = np.zeros((len(data), len(data[0])-2), dtype=np.int32)
# print(arr)


for i in range(len(data)):
    for j in range(len(data[i])-2):
        arr[i][j] = data[i][j+2]

print(arr)


#3. 각 학교의 총 학생수 > 행 기준
stdArr = np.zeros((len(data), int((len(data[0])-2)/2)), dtype=np.int32)
print(len(data))
print(int((len(data[0])-2)/2))
print(stdArr)

for i in range(len(data)):
    for j in range(int((len(data[0])-2)/2)):
        if j==0 :
            stdArr[i][j] = data[i][j+3]
        else: 
            stdArr[i][j] = data[i][3+2*j]
        
print(stdArr)

print()

print("행기준 sum",stdArr.sum(axis=1))

stdArrSum = np.insert(arr, 6, stdArr.sum(axis=1), axis=1)
print("stdArrSum", stdArrSum)

'''
stdArrSum = np.c_[arr, stdArr.sum(axis=1)]
print("sum컬럼 추가", stdArrSum)
'''

# 4. 전국 고등학교에 대해 각 학년별 총 학생수를 구하고 막대 그래프로 시각화한다
# 가로: 학년(1, 2, 3 학년), 세로: 학생수 ??
dataX = ["1학년 ", "2학년", "3학년"]
print("열기준 sum",stdArr.sum(axis=0))
'''
print("열기준 sum[0]",stdArr.sum(axis=0)[0])
print("열기준 sum[1]",stdArr.sum(axis=0)[1])
print("열기준 sum[2]",stdArr.sum(axis=0)[2])
'''

x = np.arange(3)
plt.xticks(x, dataX)
plt.bar(x, stdArr.sum(axis=0))

plt.show()




#dataY = []
# plt.xlabel("학년")
# plt.ylabel("학생수")

'''
plt.bar(x, values)
plt.xticks(x, years)

plt.show()
'''






'''     

#sum_arr = arr.sum(axis=0) 
#print(sum_arr)

  '''  




f.close()

