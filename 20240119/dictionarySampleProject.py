'''
[기초 클래스: koreait]
--> 생성자: 학생이름과 고유번호 매개변수
--> check 멤버함수
- 학생의 이름과 고유번호가 저장되어있는 딕셔너리 구현(5명만 저장) !
    입력받는 것이 아닌 키와 값을 초기화한다. dta = {"kim":"1234", "lee": "5435"}

- check 멤버함수에서 객체가 가지고 있는 이름과 고유번호를 딕셔너리안에 있는 데이터와
    비교했을 때 모두 일치하면
    "우리학원 학생이군요!" 를 출력
    아니면 "학원생이 아니군요!"를 출력
    
    

[하위클래스: student(koreait) > koreait를 상속]
def __init__(self, name, num):
    super().--init__(name, num)
    
5명의 id, pw를 딕셔너리에 초기화 해놓는다. (입력X) 

넘어온 id와 pw가 일치하면 로그인 성공을 출력!

subject() 멤버함수 매개변수 없음
로그인이 성공되었기 때문에 5개 과목과 5개듸 점수를 입력받아서 리스트에 저장

calc() 멤버함수 매개변수 없음
'''


class koreait:
    def __init__(self, name, stunum):
        self.name = name
        self.stunum = stunum

    def check(self):
        #학생의 이름과 고유번호가 저장되어있는
        #딕셔너리 구현(5명만 저장)
        #입력받는것이 아닌 키와 값을 초기화한다.
        #data = {"학생이름1":"학생의 고유번호" *5}
        data = {"kim":"111", "lee":"222", "park":"333", "jeong":"444", "han":"555"}
        if self.name in data.keys() and data.get(self.name) ==  self.stunum:
            print("우리학원 학생이군요!")
        else:
            print("학원생이 아니군요")

class student(koreait):
    def __init(self, name, num):
        super().__init__(name, num)

    def idpw(self, id1, pw):
        stdId = {"kim": "0000", "lee": "1111", "park":"2222", "jeong":"3333", "han":"4444"}
        #5명의 학생의 id와 pw를 딕셔너리에 초기화 해놓는다.
        #idpw멤버함수로 전달받은 매개변수에 저장되어있는
        #데이터(ID, PW)가 현재 딕셔너리에 일치한 정보가 있다면
        #로그인 성공 출력하고 return True,
        #아니면 로그인 실패 출력하고 return False
        pass

    def subject(self):\
        sbjList = input("enter the five subject").split()
        sbjScoreList = input("enter the five score").split()
        data = dic(zip(tuple(sbjList), tuple(sbjScoreList)))
        print("type(data)", type(data))
        #5개 과목 이름과 5개 과목 점수를
        #각각 리스트에 입력 후 zip(), dict() 함수를 이용해서 딕셔너리화

    def cal(self):
        

    def gradeshow(self):
        pass

x = student("kim", "111")
x.idpw("kim", "0000")
#student 클래그의 객체를 생성할 때 호출되는 생성자에게
#학생의 이름과 고유번호를 전달한다.
bcheck = x.check()
#x.check 함수를 통해서 우리학원 학생인지 아닌지를 판단 후
#리턴되서 돌아온 Boolean 타입을 bcheck변수에 저장

if bcheck:  #우리학원 학생이라면 이제 id와 pw를 입력하고
    #idpw 멤버함수를 호출시킨다.
    id1 = input("id입력: ")
    pw1 = input("pw입력: ")
    if x.idpw(id1.pw):
        x.subject()




















