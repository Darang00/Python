import pandas as pd

#concat( )
#result1 = pd.concat([df1, df2]) >> df1과 df2를 합침
'''
index 재배열
result2 = pd.concat([df1, df2])

'''

df1 = pd.DataFrame({
                                    'a':['a0', 'a1', 'a2', 'a3', 'a4', 'a5'],
                                    'b':['b0', 'b1', 'b2', 'b3', 'b4', 'b5'],
                                    'c':['c0', 'c1', 'c2', 'c3', 'c4', 'c5']
                                        })

'''
df2 = pd.DataFrame({
                                    'a':['a0', 'a1', 'a2', 'a3', 'a4', 'a5'],
                                    'b':['b0', 'b1', 'b2', 'b3', 'b4', 'b5'],
                                    'c':['c0', 'c1', 'c2', 'c3', 'c4', 'c5']
                                        }
                                    index = [2, 3, 4, 5, 6]
                                   )
'''
#result1 = pd.concat()

#인덱스 재정의
#result2 = pd.concat([df1, df2], ignore_index=True)

#result3 = pd.concat([df1, df2], axis=1) 행기준으로 합치기
'''
print(result2.isnull()) #nan값이 있는 자리를 Boolean 타입(True)로 돌려준다.
print(result2.isna())#isnull()함수와 동일하게 작동한다.
print(result2.fillna(0)) #fillna를 활용하게 난값이 들어가있는 자리를 사용자가 대체하는 값으로 채워진다.
'''





'''
#전치: T >> 행과 열이 바뀜
data = {"Name" : ["kim","park","han","chiol","seo"],
        "kor" :  [95,97,90,94,87],
        "eng" :  [90,86,93,85,93],
        "math" : [85,88,89,88,99],
        "coding":[100,78,65,78,53]
        }
df = pd.DataFrame(data,index=["01","02","03","04","05"])
print(df)
'''
data = {"Name" : ["kim","park","han","chiol","seo"],
        "kor" :  [95,97,90,94,87],
        "eng" :  [90,86,93,85,93],
        "math" : [85,88,89,88,99],
        "coding":[100,78,65,78,53]
        }
df = pd.DataFrame(data)
print(df)
#sum(), mean()
df1 = df.T
print("sum", df1.sum(axis=1))
print("mean", df1[1:].mean(axis=1))










'''
result3_in = pd.concat([df1, df2], axis=1, join='inner') 열방향(axis=1), 교집합(inner), 합집합(outer)


'''
