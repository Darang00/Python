import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#df = sns.load_dataset('diamonds')
#print(df)


'''
#1
df = pd.DataFrame(np.random.randn(5, 3),
                  columns=['C1', 'C2', 'C3'])

df.loc[0, 'C1'] = np.nan
df.loc[1, 'C1'] = np.nan
df.loc[1, 'C3'] = np.nan
df.loc[2, 'C2'] = np.nan
df.loc[3, 'C2'] = np.nan
df.loc[4, 'C3'] = np.nan


#ffill : forward fil _ 위에서 아래로 데이터 채운다.
#print(df.fillna(method="ffill"))
#DataFrame.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
print(df)
print(df.ffill())
print(df.where(pd.notnull(df), df.mean(), axis="columns"))
print(df.describe())
print(df.info())
print(df.head())
print(df.head(n = 10))
print(df.tail())
print(df.tail(n = 10))
print(df.fillna(df.mean())) #평균값으로 채워라

#null값이 있는지 판단하는 함수
print(df.isnull().sum())

'''




#2
#집계함수 aggFrunction
#가장 많이 활용: aggfunc = np.sum(), aggfunc = np.mean()
a1 = ['장동건', '김태희','한예슬', '한효주', '원빈', '현빈',  '차은우', '장원영', '유재석']
a2 = ["남","여","여","여","남","남","여","남","여"]
a3 = ["A","A","A","B","B","B","C","C","C"]
a4 = [97, 88, 78, 64, 84, 89, 87, 92, 99]
a5 = ["1등","2등","3등","3등","2등","1등","3등","2등","1등"]
a6 = ["수시","정시","정시","수시","수시","수시","정시","정시","수시"]
a7 = ['이름', '성별', '반', '점수', '반등수', '비고']

df = pd.DataFrame([a1, a2, a3, a4, a5, a6], index=a7, columns=list(range(1, 10)))

print("df\n", df)
print("----------------------------------------------------------------------------------")
df1 = df.T
print("df1\n", df1)
print("----------------------------------------------------------------------------------")
df1 = df1.pivot_table(values="점수", index="반",columns="성별",aggfunc="sum")
print("df1\n",df1)
print("----------------------------------------------------------------------------------")

#멀티 index
#df1 = df.pivot_table(values="점수", index = ["반", "성별"], columns = "비고", aggfunc="sum")
#print(df1)
print("----------------------------------------------------------------------------------")

df1 = df.T
#하나의 데이터만 활용 (예: 하나의 반에 1등은 1명만 있음) 
df1 = df1.pivot(values = "이름",  index="반", columns="반등수") #집계함수가 굳이 안들어감
#에러남;; cmd: pip3 install seaborn
print("pivot()\n", df1)



col = ['Machine','Country','Price','Brand']
data = [['TV','Korea',1000,'A'],
        ['TV','Japan',1300,'B'],
        ['TV','China',300,'C'],
        ['PC','Korea',2000,'A'],
        ['PC','Japan',3000,'E'],
        ['PC','China',450,'F']]
df = pd.DataFrame(data=data, columns=col)
print("df\n", df)
df1 = df.pivot(values=["Price", "Brand"], index="Machine", columns="Country")
print("df1\n", df1)



print("\n\ndiamonds----------------------------------------------------------------------------------")

df = sns.load_dataset('diamonds')
print(df)

#1. 다이아몬드의 CUT과 color 상태에 따른 평균을 구하기 (피벗 테이블)
print("1.\n")
df1 = df.pivot_table(values="carat", index="cut", columns="color",aggfunc="mean")
print(df1)

#2. 다이아몬드의 cut과 color 행 인덱스/clarity 를 columns로 중위 가격 구하기
print("\n\n2.\n")
# 넓어진 clearity열을 행으로 구하기 (고정: id_vars = [cut, color])
#df1 = df.pivot_table(values = "price", index="color", columns="clarity", aggfunc="median")
#print(df1,"\n")
#df.melt(id_vars=[cut, color], value_vars="clearity")
df1 = df.pivot_table(index=["cut", "color"], columns = "clarity", values="price", aggfunc="median")
df1 = df1.reset_index()
df1 = df1.melt(id_vars=["cut", "color"], var_name="Clarity", value_name="C_value")
print(df1)




#3. 다이아몬드의 cut, color에 따라 Price는 중위가격, carot은 
















'''
#3
df=pd.DataFrame({'store':['Costco','Costco','Costco','Wal-Mart','Wal-Mart','Wal-Mart',"Sam's Club","Sam's Club","Sam's Club"],
               'product':['Potato','Onion','Cucumber','Potato','Onion','Cucumber','Potato','Onion','Cucumber'],
               'price':[3000,1600,2600,3200,1200,2100,2000,2300,3000],
                'quantity':[25,31,57,32,36,21,46,25,9]})

print(df.melt(id_vars=['product','store']))

'''
