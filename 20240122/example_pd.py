'''
cmd 창: pip3 install pandas
>>pyarrow dependency 에러 난다면 pip install pyarrow 이것도 설치해야됨;;

import pandas as pd
data = pd.Series([100, 200, 300, 400])
print(data)

'''
import pandas as pd

'''
data = pd.Series(["100", 200, 300, 400])
print(data)
print(type(data))
'''

data1=[1, 2]
data = {"a":100, "b":200, "c":200, "d":300}
s = pd.Series(data)
print(s["a"])
print(s[0:3])
print(s[["a", "b"]])

#추가
s["e"] = 400

print("s", s)

list1 = [1, 2, 3, 4, 5]
print(list1[0])

'''
판다스, 넘파이
리스트에 수강 과목 입력 후 저장(갯수 제한 없음)
리스트에 수강 과목 점수 입력 후 저장(갯수 제한 없음)
시리즈 객체에 입력받은 과목 리스트와 점수 리스트 저장
과목점수만 뽑아와서 총합과 평균을 구한다.
그 후 시리즈 객체에 총합과 평균을 각각 구한다.
'''
print("==========================================")
sub = input("enter the subjects ").split()
score = list(map(int, input("enter the scores ").split()))

print(sub)
print(score)

'''
subList = tuple(sub)
scoreList = tuple(score)

data = dict(zip(subList, scoreList))
print(data)
s = pd.Series(data)
print("Series\n", s)
print("data.index", s.index)
print("data.index", s.values)
print("data.index", s.name)
'''

data = pd.Series(score, index = sub)

i = data.index
print("i\n", i)
v = data.values
print("v\n", v)
add = v.sum()
print("add\n", add)
avg = v.mean()
print("avg\n", avg)
#그 후 시리즈 객체에 총합과 평균을 각각 추가한다.
data["총합"]=add
data["평균"] = avg



































































