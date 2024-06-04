import csv
#open(): 파일 열기 , close(): 파일 닫기
f = open("month_temp.csv", "r", encoding="UTF-8")
#파일명.확장자, 읽기모드, 문자종류
#"test.csv" 파일 객체가 f 에 저장됨
#본 소스코드파일이 저장된 위치에 열고자 하는 .csv 파일이 존재해야 정상적으로 실행됨.

lines = csv.reader(f)
#print(lines)
'''
for i in lines :
    #print(i)
    if "2019-10-05" in i:
        print(i)
    
f.close()
'''

'''
#split() 함수 > ['119', '2019-10-05', '18.9', '15.7', '22'] 에서 -를 없애라
for i in lines :
    if "2019-10-05" in i:
        seperate =i[1].split("-")    #i.split("-") 에러남. 'list' object has no attribute 'split'  > split은 string에만 사용 가능한가봄?
        print(seperate)
        print(type(seperate))   #<class 'list'> split함수로 분리된 단어들은 list에 담긴다.
    
f.close()
'''

'''
#10월 1일 ~ 10월 31일까지의 평균 기온
for i in lines :
    print(i[2])
    
f.close()
'''

'''
#10월 1일 ~ 10월 31일까지의 평균 기온
for i in lines :
    print(i)
    
f.close()
'''


'''
data = []
for i in lines :
    data.append(i[2])

print(data)
    
f.close()
'''

'''
#제목 빼고 출력
head = next(lines) #커서를 다음줄로 이동
print(head)

for i in lines :
    print(i)

f.close()
'''
    


'''
#일자만 출력하는데 연도 빼고 월, 일만 출력해라.
head = next(lines)
for i in lines:
    date = i[1]
    print(date[5:]) #또는 print(i[1][5:]) 

f.close()
'''


'''
#csv에서 가져오는 데이터는 모두 string 타입
head = next(lines)
for i in lines:
    print(float(i[3]))

f.close()
'''

#일교차 (최고기온[4] - 최저기온[3])
head = next(lines)
#제목: 일자 최저기온 최고기온 일교차
print("%s %s %s %s"%("일자", "최저기온", "최고기온", "일교차"))
for i in lines:
    tmp = float(i[4]) - float(i[3])
    #%.1f : 소수점 1자리 수까지 표현해라 
    print("%s %.1f %.1f %.1f"%(i[1], float(i[3]), float(i[4]), float(tmp)))


f.close()







