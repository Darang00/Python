#school_2019.csv
import numpy as np
import csv
f = open("school_2019.csv", "r", encoding="utf-8")
lines = csv.reader(f)

data = np.array([
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]
                    ])

x = len(data[0]) #data[0] 의 길이 (값이 0으로 3개 들어있으므로 3 출력됨)
#print(x)

cnt = 1
tot = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = cnt
        tot = tot+cnt
        cnt = cnt+1
        
     
print(data)
print("Sum of data: ",tot)

print("------------------------------------------")
#ㄹ 모양으로 숫자열 진행
cnt2 = 1
for i in range(len(data)):
    if i%2==1 :
        for j in range(len(data[i])):
            data[i][2-j]=cnt2
            cnt2 = cnt2 + 1
    else:
        for j in range(len(data[i])):
            data[i][j]=cnt2
            cnt2 = cnt2 + 1

print(data)
print("------------------------------------------")

#다른방법
data = np.zeros((5, 5), dtype="int32")

#외각에 -1을 채우기 
for i in range(len(data)) :
    data[0][i]=-1
    data[i][0]=-1
    data[4][i]=-1
    data[i][4]=-1

i=1
j=1
flag=0
cnt=1
data[i][j]=cnt

while True :
    if cnt >25 :
        break
    
    if flag ==0:
        if data[i][j+1] == 0 :
            j=j+1
            cnt = cnt+1
            data[i][j] = cnt

    else :
        flag = 1
        i=i+1

    if flag ==1:
        if data[i][j-1] == 0 :
            j=j-1
            cnt = cnt+1
            data[i][j] = cnt

    else :
        flag = 0





















'''
arr=[]
for i in lines:
    arr.append(i)

    print(arr)
'''

