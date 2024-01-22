import numpy as np
import pandas as pd
import csv

file = open("classtest.csv", "w", encoding="utf-8", newline="")  # csv파일을 쓰기 모드로 열기
wr = csv.writer(file)

# 헤더의 이름으로 "이름", "평균"을 csv파일에 쓰기
# 학원 재원생의 이름과 평균점수를 담을 수 있는 딕셔너리 생성
stu = []
total_stu = {}

class koreait:
    def __init__(self, name, stunum):
        self.name = name
        self.stunum = stunum

    def check(self):
        data = {"kim": "1234",
                "lee": "1234",
                "park": "1234",
                "nam": "1234",
                "seo": "1234"}

        if data[self.name] == self.stunum:
            print("우리 학교 학생이군요")
            return True
        else:
            print("우리학교 학생이 아니군요!")
            return False
    def manage(self):
        # 학원재원생의 이름과 평균을 저장역할을 하는 함수와 딕셔너리 생성 후
        #학생의 이름(key) : 학생의 평균(value)를 저장 후 딕셔너리 출력
        total_stu[self.name] = self.avg
        print("total_stu\n", total_stu)

        wr.writerow([self.name, self.avg])
    
class student(koreait):
    def __init__(self, name, num):
        super().__init__(name, num)

    def idpw(self, id1, pw):
        data = {"chankb13": "1234",
                "chankb36": "1234"}

        if data[id1] == pw:
            print("로그인성공")
            return True
        else:
            return False

    def subject(self):
        self.sbjt = input("enter the subjects: ").split()
        self.score = list(map(int, input("enter the scores: ").split()))


    def calc(self): 
        self.dataDict = dict(zip(self.sbjt, self.score)) #딕셔너리로 묶을 때 굳이 튜플로 변환할 필요 없음. 리스트 두개 묶어서도 가
        print(self.dataDict)
        # 수강 과목과 수강 점수 리스트를 합쳐서 딕셔너리에 저장
         # 넘파이를 활용하여 값(딕셔너리에 저장된 점수)들을 넘파이 배열에 저장
        v= self.dataDict.values() #dictionary 는 값 빼올 때 "함수"!!!
        print("v??? ", v)
        self.npScore = np.array(list(v))
        print("npScore", self.npScore)
        self.sum = self.npScore.sum()
        self.avg = self.npScore.mean()
        
        # 배열에 저장되어있는 값들의 총합
        print("npScoreSum(총점)", self.sum)
        # 배열에 저장되어있는 값들의 평균
        print("npScoreAvg(평균)", self.avg)
        # 총점과 평균 출력

    def gradeshow(self):
        # 객체가 가지고 있는 평균 점수를 활용해서 (A~F)학점 구한 후 변수에 객체 변수에 저장
        scoreAvg = self.npScore.mean()
        self.grade = ""
        if scoreAvg >=90 :
            self.grade = "A"
        elif 80<= scoreAvg <90:
            self.grade = "B"
        elif 70<= scoreAvg <80:
            self.grade = "C"
        elif 60<= scoreAvg <70:
            self.grade="D"
        else :
            self.grade="F"

        # grade 변수에 학점 저장 (A~F)
        print("self.grade ", self.grade)


    def grade_table(self):
        # 총점과 평균, 학점 시리즈 만들기
        print(f"{self.name}님의 각 과목의 점수와 총점과 평균입니다")
        # 수강 과목이름과 수강과목 점수가 저장되어있는 딕셔너리를 시리즈 객체 타입으로 만들기
        subScore = pd.Series(self.dataDict)
        print("subScore\n",subScore)
        print(type(subScore)) #<class 'pandas.core.series.Series'>
          
        # 객체가 저장하고 있는 수강 과목의 총점을 시리즈 객체에 추가
        subScore["총점"] = self.sum   
         
         # 객체가 저장하고 있는 수강 과목의 평균을 시리즈 객체에 추가
        subScore["평균"] = self.avg
         
        # 객체가 저장하고 있는 수강 과목의 학점(A 또는 F)를 시리즈 객체에 추가
        subScore["학점"] = self.grade
          
        # 시리즈 객체 출력
        print("subScore\n", subScore)
        # 상위 클래스의 manage()호출
        super().manage()



x = student("kim", "1234") #stu는 list
y = student("park", "1234")
stu.append(x)
stu.append(y)
print("stu: ", stu)
headerList = ["Name", "AvgScore"]
wr.writerow(headerList) #header 만들기

for i in range(2):   
    bcheck = stu[i].check()

    if bcheck:
        id1 = input("id 입력 : ")
        pw = input("pw 입력 : ")
        if stu[i].idpw(id1, pw):
            stu[i].subject()
            stu[i].calc()
            stu[i].gradeshow()
            stu[i].grade_table()

file.close()
