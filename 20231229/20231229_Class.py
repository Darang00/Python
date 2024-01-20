class car : #틀 (공장)

    def car_color(self, x, y) :  #메서드
        #매개변수 'self'에는 현재 호출한 객체 저장 (객체를 통해서 메서드가 호출될 시 이름을 'self'로 약속)
        #print("이곳은 색 동장을 하는 곳입니다.")
        print('self???  ', self) #self는 genesis 라는 객체의 "주소"를 가지고 있는거 같음...?
        self.x = x
        self.y = y
        print(self.x, self.y)
        
    def car_option(self) : #메서드
        print("이곳은 옵션을 달아주는 곳입니다.")


'''
#car 클래스(공장)에서 제네시스라는 "객체" 생성
genesis = car()
print(genesis)

# '.'은 연결 연산자
genesis.car_color(3, 5)
genesis.car_option()



#sonata 객체 생성
sonata = car()
print(sonata)
sonata.car_color(10, 20)
#sonata.car_option()
'''




#예
class FourCal:
    def __init__(self, first, second): #생성자(constructor)
         self.first = first
         self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return sesult


'''
a = FourCal()
a.setdata(4, 2)
result_a = a.add()
print('result_a   ', result_a)

b = FourCal()
b.setdata(3, 7)
result_b = b.add()
print('result_b   ', result_b)

y = a.add()
x = b.add()
print(x, y)

c = FourCal()
c_1 = int(input())
c_2 = int(input())
c.setdata(c_1, c_2)
result_c = c.add()
print('result_c   ', result_c)
'''

a = FourCal(4, 2)
b = FourCal(3, 7)
print(a) #a의 주소
print(b) #b의 주소
print(a.first, a.second)
print(b.first, b.second)



















#생성자(constructor)
#객체가 생성될 때 자동으로 호출되는 메서드
#파이썬 메서드명으로 __init__ 를 사용하면 이 메서드는 생성자가 된다.




