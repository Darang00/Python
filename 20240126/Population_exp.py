'''
전달된 소스파일을 데이터프레임으로 바꾸기
국내 전체 인구수 세대수 남녀 인구수 합계 구하기

'''
import csv
import pandas as pd

file = open("population_2020.csv","r",encoding = "utf-8")

x = csv.reader(file)
head =next(x)
list_data=[]
list_temp = []
dict_data={}

def get_dict(list_data,keys,dict_data) :
    area = get_area(list_data[0])
    dict_data.update({keys[0] :area}) #지역 키에 값으로 서울~제주도 저장


    for i in range(1,7) :
        if i==3 or i==6 :
            data =del_comma(list_data[i],"float")
        else :
            data = del_comma(list_data[i],"int")
        dict_data.update({keys[i] : data})

def get_area(data) :
    tmp = []
    for x in data :
        arr = x.split()
        tmp.append(arr[0])

    return tmp
def del_comma(data,t) :
    tmp = []
    for x in data :
        string = ""
        arr=x.split(",")
        for i in range(len(arr)) :
            string+=arr[i]
        if t=="intiger" :
            tmp.append(int(string))
        else :
            tmp.append(float(string))
    return tmp

##########################################
# csv파일에 저장된 데이터를 2차원으로 리스트로 저장 
for i in x :
    list_temp.append(i[:])
#print(list_temp)
for i in range(7) :
    temp=[]
    for j in range(len(list_temp)) :
        temp.append(list_temp[j][i]) # 행과 열을 바꿈. 
    list_data.append(temp)
print(list_data)
##########################################
# 리스트를 딕셔너리로 변환
keys = ["지역","총인구수","세대수","세대당_인구","남자_인구수","여자_인구수","남여_비율"]

get_dict(list_data,keys,dict_data)

print(dict_data)
print("--------------------------------------------------------------")

#데이터프레임 출력
popDf = pd.DataFrame(dict_data)
print("popDf\n", popDf)
print("--------------------------------------------------------------")

#총 인구수 기준으로 내림차순으로 정렬
popDesc = popDf.sort_values('총인구수', ascending=False)
popDescReidx = popDesc.reset_index(drop=True)
print("popDescReidx\n", popDescReidx)
print("--------------------------------------------------------------")

#국내 전체 인구수, 세대수, 남여 인구수, 합계
totPop = popDf['총인구수'].sum()
print("totPop:", totPop)

totCom = popDf['세대수'].sum()
print("totCom:", totCom)

totPopMale = popDf['남자_인구수'].sum()
print("totPopMale:", totPopMale)

totPopFemale = popDf['여자_인구수'].sum()
print("totPopFemale:", totPopFemale)

totPopDf = popDf[['총인구수', '세대수', '남자_인구수', '여자_인구수']].sum()
print("final\n", totPopDf)

print("--------------------------------------------------------------")
df1 = popDf.loc[:, ['총인구수', '세대수', '남자_인구수', '여자_인구수']].sum()
print("df1\n", df1)
print(type(df1)) #<class 'pandas.core.series.Series'>

print("--------------------------------------------------------------")
print("df1.to_frame()\n", df1.to_frame())
print(type(df1.to_frame()))
print(" df1.to_frame().T\n",  df1.to_frame().T)

print("--------------------------------------------------------------")

#각 지역의 총인구와 세대수를 그래프로 시각화!
df = pd.DataFrame(dict_data)
index = ["서울", "부산", "대구", "인천", "광주", "대전"]
dx = df.iloc[:6, 1]
print("dx", dx)
dx = df.values.tolist()


dy = df.iloc[:6, 2]
print("dy", dy)
dy = df.values.tolist()


df1 = pd.DataFrame({ "총인구수":dx, "총세대수":dy}, index = index)
                                    
#a = df1.plot.bar()

























file.close()
