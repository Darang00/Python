import matplotlib as plt
import pandas as pd
df   = pd.read_csv("scientists.csv")
print(df)
print(df.describe())

#평균 나이보다 많은 과학자?

ages = df["Age"]

print(ages[ages>ages.mean()])


#평균나이보다 많은 과학자들
print(df["Age"]>df["Age"].mean()) #행을 뽑아오는거

print(df[df["Age"]>df["Age"].mean()]) #데이터프레임에 저장된 평균나이보다 많은 과학자들의 정보가 전체 행으로 뽑아져서 출력된다(Boolean 타입 반환X)
print("---------------------------------------")

born = pd.to_datetime(df["Born"], format="%Y-%m-%d")
died = pd.to_datetime(df["Died"], format="%Y-%m-%d")

df["born_dt"], df["died_dt"] = (born, died)
print("born\n", born)
print("df\n", df)

print("---------------------------------------")

#과학자들의 실제 나이 구하기
#df["born_dt"], df["died_dt"] = (born, died)
df["age_days"] = df["died_dt"]-df["born_dt"]
print(df)

print("---------------------------------------")


#열, 행 삭제
#drop() 함수
df = df.drop(["Age"], axis="columns") #열 삭제
print(df)
print("---------------------------------------")
df = df.drop([5, 6], axis = 0) #5, 6번 행 삭제
print(df)





















