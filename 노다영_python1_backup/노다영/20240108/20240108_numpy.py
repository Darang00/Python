#numpy--> Numerical Phthon
#가장 큰 특징: n차원의 배열을 생성하고 사용할 수 있다.
#파이썬의 고성능 수치계산을 위한 라이브러리
#여러 형태의 벡터 및 행렬 연산과 나아가 여러 수학적인 기능들을 빠르고 간편하게 사용할 수 있는 기능들을 제
#--> ndarray
'''
데이터 분석과 산술 연산을 하는 데 있어서 가장 기본적으로 많이 사용되는 패키지입니다.
산술연산, 통계함수, 배열의 조건식, 열과 행을 삽입해주는 함수 등 다양한 기능을 제공해준다.

'''

import numpy as np
#ndarray 객체를 생성하는 방법. (1차원 배열)

#data=np.array([1, 2, 3, 4, 5])
#data=np.random.rand(2, 3) #2차원 배열, 한 행에 3개의 수가 들어감 (2행 3열짜리 만들어라)
#data=np.zeros((5, 5), dtype=np.int32)
#data = np.ones(8, dtype=np.int32)
#data=np.arange(1, 10, 2)

'''
data=np.zeros((5, 5), dtype=np.int32) #zeros 함수: 0으로 초기화 

print(data)
#print(type(data))
print(data.dtype)

data2 = np.ones((3, 4), dtype=np.int32)     #3행 4열
print(data2)
print(data2.dtype)


data3 = np.arange(1, 10, 2)
print(data3)
print(data3[2])
print(data3[2:4])
print(data3.dtype)


data3[2:4] = 10     #슬라이싱을 통해서 해당 인덱스에 값을 통째로 바꿀 수 있다. 
print(data3)
print(data3.dtype)
print(data3.shape)
'''


'''
2차원 배열은 1차원 배열의 집합니다.
'''
#2차원배열의 데이터 추출
data4=np.array([
                        [80, 78, 90, 93],
                       [65, 87, 88, 75],
                      [98, 100, 68, 80]
                   ])
print(data4)

'''
print(data4[0][2]) #0, 2에 있는거 꺼내라 (해당 좌표의 데이터만 추출
print(data4[0][1:]) #0행의 1열부터 마지막 인덱스까지의 데이터를 추출, 근데 리스트 형태로 [] 이거랑 같이 나옴
print(data4[0]) #0행 전체 데이터를 가져온다.
print(data4[[0, 1]])
#두 개 이상의 행을 가져올 때는 밖에 [] 연산자를 한번 더 씌워줘야 한다.

print()
print()
print()
#data4[1] = 50 #1행에 있는거 다 50으로 바꿈
#data4[:] = 25 #전체 행, 전체 열에 저장된 데이터를 다 25로 바꿈
print(data4)
'''

'''
#2차원 배열의 산술연산
cpy = data4*2 #data4의 각각의  데이터들에 모두 2씩 곱하기   
print(cpy)

arr = data4*data4 #제곱 연산
print(arr)

#관계연산자 활용
x = cpy >arr    #저장되는 데이터 타입이 Boolean 타입.
print(x)
'''

#배열의 통계함수   
#합계, 평균, 최대값, 최솟값, 최대값의 위치, 최솟값의 위치
'''
print("data4.sum()", data4.sum())
print("data4.mean()   ", data4.mean())
print("data4.max()   ", data4.max())
print("data4.min()   ", data4.min())
print(data4.max(axis=0))
print(data4.max(axis=1))
#axis(축)  = 0 --> 열을 기준으로 가장 큰 값을 돌려준다. 배열로 
#axis(축)  = 1 --> 행을 기준으로 가장 큰 값을 돌려준다. 배열로
'''

index1 = np.argmax(data4, axis=0) #열을 기준으로 최대값인 수의 index를 반환
print(index1)
index2 = np.argmin(data4, axis=1) #[1 0 2]
print(index2)








