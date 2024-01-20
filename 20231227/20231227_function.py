'''
for 변수 in range(횟수):
     반복할 코드
'''

'''
함수

내장함수(도구)
print() : 출력을 담당하는 기능
input()
range()
int()
float()
list()
duple()


사용자 정의 함수
 함수를 정의하는 방법
 1. def (정의 / definition)
 2. 함수 이름을 작성한다.
 3. ( )
 4.  :
 5. 들여쓰기해서 블럭 안에 실행문장 작성
 6. 함수를 "호출(call)"하면 해당 함수 실행
 7. 함수가 종류가 되면 자기자신을 호출한 곳으로 되돌아온다.



 1. 전달인자 없고, 매개변수 없는 타입
 2. 전달인자O, 매개변수O
 3. 전달인자X, 매개변수X, 리턴타입O
 4. 전달인자O, 매개변수O, 리턴타입O


'''

'''
#함수 선언
#1. 전달인자 없고 매개변수 없는 타입
def test() : #받아주는 데이터를 "매개변수"로 한다.
    #블럭 안에 실행문장 작성
    print("hello world!")
'''


'''
10번 반복해서 test() 함수 호출
for i in range(10):
    test()
'''

'''
#함수를 호출
test() #전달되는 데이터를 "인자"라고 한다.
'''

'''
#Q. 함수 안에서 두 개의 정수를 입력받고 입력받은 두 정수의 합을 구한 후 출력
def test1() :
    x = int(input())
    y = int(input())
    print(x + y)

test1()
'''

'''
#Q. 전달인자 O, 매개변수O
def test2(x, y) :
    print(x, y)

test2("hello", "coding")
'''


'''
#2번타입. 함수 안에서 두 개의 정수를 입력받고 입력받은 두 정수의 합을 구한 후 출력: 전달인자, 매개변수 있는거
def test3(x, y):
    print(x + y)
    
#호출방법1
x = int(input())
y = int(input())
test3(x, y)

#호출방법2
test3(int(input()), int(input()))
'''


'''
# 3. 전달인자X, 매개변수X, 리턴타입O
def test4() :
    return 10, 20
    #리턴을 만나면 함수가 즉시 종료되고 데이터를 반환한다. >> 자기자신을 호출한 곳으로 되돌아온다.

x, y = test4()
print(x + y) #10
'''


'''
# 3번타입. 덧셈 연산 후 결과를 "저장"하고 리턴한다.
def test5():
    x = int(input())
    y = int(input())
    z = x + y
    return z

x = test5() #변수에 담아주는거 잊지 말자.. 리턴받은 거를 변수에 "저장"
print(x)
'''


'''
# 4번타입. 덧셈 연산 후 결과를 "저장"하고 리턴한다.
def test6(x, y):
    z = x + y
    return z

x = test6(10, 20) #변수에 담아주는거 잊지 말자.. 리턴받은 거를 변수에 "저장"
print(x)
'''



#사칙연산 각 함수들을 모두 정의한다.
#함수 밖에서 정수 두 개 입력 받고 각 함수의 역할 수행 후 결과를 출력한다. + - * / %
'''방법1
def plus(x, y):
    print(x + y)

def minus(x, y):
    print(x - y)

def times(x, y):
    print(x * y)

def devide(x, y):
    print(x/y)

def rest(x, y):
    print(x%y)

x = int(input())
y = int(input())
plus(x, y)
minus(x, y)
times(x, y)
devide(x, y)
rest(x, y)
'''''''''''''''''''''
''''''''''''''''
#방법2
def plus1(x, y):
    return x + y

def minus1(x, y):
    return x - y

def times1(x, y):
    return x*y

def devide1(x, y):
    return x/y

def rest1(x, y):
    return x%y

x = int(input())
y = int(input())

p = plus1(x, y)
m = minus1(x, y)
t = times1(x, y)
d = devide1(x, y)
r = rest1(x, y)

print(p)
print(m)
print(t)
print(d)
print(r)

'''''''''''''''''''''






'''
변수의 라이프 사이클
지역변수와 전역변수
'''

'''
x = 10          #전역변수
def foo():
    print(x)     #전역변수 출력


foo()
print(x)
'''

'''
def foo():
    x =     # foo의 지역 변수
    print(x)    # foo의 지역 변수 출력

foo() #foo() 실
print(x) #name 'x' is not defined
'''


'''
x = 10
def foo():
    x = 20
    print(x)

foo()
print(x) #프로그램 끝나면 global x 삭제됨
'''


x = 10
def foo():
    global x
    x = 20
    print(x)

foo()
print(x)




















    

