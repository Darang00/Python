import csv
#open(): 파일 열기 , close(): 파일 닫기
f = open("test.csv", "r", encoding="utf-8")
#파일명.확장자, 읽기모드, 문자종류
#"test.csv" 파일 객체가 f 에 저장됨
#본 소스코드파일이 저장된 위치에 열고자 하는 .csv 파일이 존재해야 정상적으로 실행됨.

lines = csv.reader(f)
#print(lines)

for i in lines :
    print(i)
    print(type(i))

f.close()

    
