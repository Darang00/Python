#6102 : [numpy] arange

import numpy as np

#1.
data = np.zeros(40, dtype=np.int32)
cnt = 10
for i in range(len(data)):
    data[i] =cnt
    cnt = cnt+1

print(data)


#2.
cnt = 10
for i in range(len(data)):
    data[len(data)-1-i] = cnt
    cnt = cnt+1
    
print(data)


#3.
data = np.array(np.zeros(9, dtype=np.int32))
print(data)

dataM = np.reshape(data, (3, 3))
cnt = 0
for i in range(dataM):
    dataM[i] = cnt
    cnt = cnt+1

print(dataM)


    
