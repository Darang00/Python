import numpy as np
#numpy 없을 때 설치하는 명령어 pip3 install numpy

data1 = np.zeros((3, 3),  dtype=np.int32)

print("기본모양------------------------------------------")
cnt1 = 1
for i in range(len(data1)): 
    for j in range(len(data1[i])):
        data1[i][j] = cnt1
        cnt1 = cnt1+1

print(data1)

print("ㄹ모양------------------------------------------")
data2 = np.zeros((3, 3),  dtype=np.int32)
cnt2 =1
for i in range(len(data2)):
    if i%2 == 0:
        for j in range(len(data2[i])):
            data2[i][j] = cnt2
            cnt2 = cnt2+1
    else:
         for j in range(len(data2[i])):
             data2[i][2-j] = cnt2
             cnt2 = cnt2+1
        
print(data2)

print("i를 채워서 만드는 방법?------------------------------------------") #나중에 고쳐보자..
data3 = np.zeros((5, 5), dtype="int32")
for i in range(len(data3)):
    data3[0][i] = -1
    data3[i][0] = -1
    data3[4][i] = -1
    data3[i][4] = -1


i = 1
j = 1
flag = 0
cnt3 = 1
data3[i] = cnt3

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





    
