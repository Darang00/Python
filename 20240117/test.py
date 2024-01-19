'''
이름
성별
나이
주소
전화번호 
'''
'''
x = "kim"
gender = "남자"
age = 20
adr = "분당"
ph = "010-1234-1342"
'''

class FourCal:
    def setdata(self, first, second):
         print("self", self) #self는 객체의 주소 가지고 있음 
         self.first = first
         self.second = second

    def add(self):
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(4, 2)

b = FourCal()
b.setdata(3, 1)
