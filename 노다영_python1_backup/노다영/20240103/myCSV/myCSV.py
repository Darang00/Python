import csv
#open(): 파일 열기 , close(): 파일 닫기
fw = open("한국고용정보원_직업별_임금정보_20230908.csv", "r", encoding="cp949")
#파일명.확장자, 읽기/쓰기모드, 문자종류
#"test.csv" 파일 객체가 f 에 저장됨
#본 소스코드파일이 저장된 위치에 열고자 하는 .csv 파일이 존재해야 정상적으로 실행됨.

lines = csv.reader(fw)

'''
#임금 상위 25[1] - 하위25[3]
for i in lines:
    #print(i)
    if  '의사' in i[0] or '약사' in i[0]:
        tmp = float(i[1]) - float(i[3])
        print(i[0], format(tmp, ".0f"))
        
fw.close()
'''

'''
#임금 대표값의 평균
for i in lines:
    #print(i)
    if  '의사' in i[0] or '약사' in i[0]:
        tmp = (float(i[1]) + float(i[2]) + float(i[3]))/3
        print(i[0], format(tmp, ".1f"))
        
fw.close()
'''

#의사아닌사람들
head = next(lines)
for i in lines:
    #print(i)
    if  '의사' not in i[0]:
        print(i)
        
fw.close()



    
