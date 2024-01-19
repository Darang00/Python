import numpy as np
#배열에 조건식 사용
data1 = np.random.randn(3, 4)
print(data1)
print(data1>0) #Boolean 타입으로 반환한다.

tot = (data1<0).sum() #data에 들어있는 데이터 중 0보다 작은것을의 개수를 세라 
print(tot)

#where
data2 = np.where(data1>0, 1, -1) #data배열에 저장된 데이터 중 1번째 조건식이 참이면 1, 거짓이면 -1 반환
print(data2)



#데이터 정렬
data = np.array([
                        [80, 78, 90, 93],
                        [65, 87, 88, 75],
                        [98, 100, 68, 80]
                    ])

#data.sort(1) #--> 행기준 정렬 (오름차순인듯?)
data.sort(0) #--> 열기준 정렬 
print(data)



print()
print()
print()

data0 = np.array([
                        [1, 1, 1],
                        [2, 2, 2],
                        [3, 3, 3]
                    ])

#arr = np.array([1, 2, 3, 4, 5])
arr2 = np.insert(data0, 2, 10, axis=1)
#insert(배열이름, 인덱스, 데이터)
print(arr2)
