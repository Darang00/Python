import numpy as np
import csv

f = open("school_ex.csv",  "r", encoding="utf-8")
'''
지역, 학교명, 학급수, 학생수, 교사수  >> header
분당, 분당초, 28, 110, 32  >>data
서울, 강남초, 31, 223, 23
용인, 용인초, 45, 343, 22

'''


x = csv.reader(f)

head = next(x)
print("head", head)

print()

#1차원의 리스트를 2차원 리스트로 바꿔줘야 한다.
data=[]
for i in x:
    data.append(i[:]) #i행에 있는 모든 데이터를 data에다가 넣음.

print(data)


#Q1.numpy 배열에 학급수, 학생수, 교사수만 저장될 수 있도록 만든다.
arr = np.zeros((len(data), len(data[1])-2), dtype=np.int32)
print(arr)

for i in range(len(data)):
    for j in range(len(data[i])-2):
       arr[i][j] = data[i][j+2]

print(arr)


'''
#최대 학급수
maxClassIdx = np.argmax(arr, axis=1)
print("maxClassIdx", maxClassIdx)

maxClass = arr[1][1]
for i in range(len(arr)):
    for j in range(len(maxClassIdx)):
        if arr[i, maxClassIdx[j]] >maxClass :
            maxClass = arr[i, maxClassIdx[j]]
'''


#최대학급수 가진 학교
max_index = np.argmax(arr, axis=0)
max_school = data[max_index[0]][1]
print(max_index)
print("max_school", max_school)

#최대 학급수
max_class = data[max_index[0]][2]
print("max_class", max_class)


#최대 학생수 
max_std = data[max_index[1]][3]
print("max_std", max_std)

#최대 교사수
max_tch = data[max_index[2]][4]
print("max_tch", max_tch)








'''
arr = np.zeros((5, 5), dtype=np.int32)
cnt=1
for i in range(5):
    for j in range(5):
        arr[i][j] = cnt
        cnt +=1
'''


f.close()

















'''
data = np.array([ [80, 78, 90, 93],
                                [65, 87, 88, 75],
                                [98, 100, 68, 80] ])

print(data.sum())
print(data.mean())
print(data.max())
print(data.min())

#axis=0: 열기준, axis=1: 행기준 
print(data.max(axis=0)) # [98 100 90 93] >>list가 아닌, numpy  배열로 반환
print(data.max(axis=1)) # [93 88 100]


index1 = np.argmax(data, axis=0)    # "열"을 기준으로 최대값의 인덱스를 반환한다. 
index2 = np.argmin(data, axis=1)     # "행"을 기준으로 최소값의 인덱스를 반환한다.  
print(index1) #[2 2 0 0]
print(index2) #[1 0 2]
'''
