import pandas as pd
import csv

'''1.
data = {"이름":["kim", "park", "lee", "seo"],
                "ID":["aaa", "bbb", "ccc", "ddd"],
                "PW":["1234", "1234", "1234", "1234"]
            }

print(type(data)) #<class 'dict'>

df = pd.DataFrame(data)
print(df)
print(type(df)) #<class 'pandas.core.frame.DataFrame'>
'''


'''2.
data = {"이름":["kim", "park"],
                "나이":[23, 35],
                "번호":["010-1234-0000", "010-1234-8888"]
            }

df = pd.DataFrame(data, columns = ["이름", "번호", "나이", "주소"], index=["01", "02"])
print(df)
print(type(df)) #<class 'pandas.core.frame.DataFrame'>

'''


'''
#loc, iloc (loc: location의 약자)
data = {"학교":["분당고", "서울고", "강남고", "하나고", "외대부고"],
                "학급수":[23, 35, 15, 19, 10],
                "학생수":["620", "600", "550", "580", "400"],
                "교사수":["89", "95", "70", "90", "65"]
            }

df = pd.DataFrame(data, index = ["01", "02", "03","04", "05"])
print(df)
print("df.loc[01]\n", df.loc["01"])
x = df.loc["01"]
print("type(x)", type(x)) #type(x) <class 'pandas.core.series.Series'>
'''




'''
#여러행 가져오기
data = {"학교":["분당고", "서울고", "강남고", "하나고", "외대부고"],
                "학급수":[23, 35, 15, 19, 10],
                "학생수":["620", "600", "550", "580", "400"],
                "교사수":["89", "95", "70", "90", "65"]
            }

df = pd.DataFrame(data, index = ["01", "02", "03","04", "05"])
print(df.loc[["01", "03", "05"]]) #여러행 추출 >> [[   ]] : 여러 행 가져올때는 리스트로 만들어야함.
x = df.loc[["01", "03", "05"]]
print("type(x)", type(x)) #type(x) <class 'pandas.core.frame.DataFrame'>
'''


'''
#모든행 가져오기
data = {"학교":["분당고", "서울고", "강남고", "하나고", "외대부고"],
                "학급수":[23, 35, 15, 19, 10],
                "학생수":["620", "600", "550", "580", "400"],
                "교사수":["89", "95", "70", "90", "65"]
            }

df = pd.DataFrame(data, index = ["01", "02", "03","04", "05"])
print("df.loc", df.loc[:, ["학교", "학생수"]])
print("열만 [ ]\n", df["학교"]) #데이터 프레임 객체로 반환
print("열만[[ ]]\n", df[["학교"]]) #시리즈 객체 타입
#print("df.컬럼명\n", df."학교")
x = df.loc[:, ["학교", "학생수"]]
print("type(x)", type(x)) #type(x) <class 'pandas.core.frame.DataFrame'>
print("========================")
'''

#1.하나의 행 출력
#2. 여러 행 출력
#3. 모든 행의 3개 열 출력
'''
data_iloc = {"학교":["분당고", "서울고", "강남고", "하나고", "외대부고"],
                "학급수":[23, 35, 15, 19, 10],
                "학생수":["620", "600", "550", "580", "400"],
                "교사수":["89", "95", "70", "90", "65"]
            }
df_iloc = pd.DataFrame(data_iloc)
print("df_iloc", df_iloc)
print("-----------------------------------------")
print("하나의 행만 출력\n", df_iloc.iloc[0])
print("-----------------------------------------")
print("첫 2개의 행만 출력\n",df_iloc.iloc[0:2])
print("-----------------------------------------")
print("모든 행의 3개 열 출력\n",df_iloc.iloc[:, [0, 1, 2]])


'''


data = {"Name":["kim", "park", "eng", "math", "coding"],
                "Kor":[95, 97, 90, 94, 87],
                "Eng":[90, 86, 93, 95, 93],
                "Math":[85, 88, 89, 88, 99],
                "Coding":[100, 78, 65, 78, 53]
            }

df = pd.DataFrame(data, index = ["01", "02", "03","04", "05"])
print(df)

df2 = df.iloc[:, [1, 2, 3]]
print(df2)
print("type(df2)", type(df2)) #<class 'pandas.core.frame.DataFrame'>
tot = df2.sum(axis=1)
print(tot)
print("type(tot)", type(tot)) #<class 'pandas.core.series.Series'>
avg = df2.mean(axis=1)
print(avg)
print("type(avg)",type(avg)) #<class 'pandas.core.series.Series'>

print("=======================")
print("이름 합계 평균") #반복문
df3 = df.iloc[:, [0]] #이름

for i in range(5):
    print(df.iloc[i, 0], tot.iloc[i], avg.iloc[i])
    

































