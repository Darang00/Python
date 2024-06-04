class FourCal: #상위 / 슈퍼 / 베이스 / 부모 클래그
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self) :
        result = self.first + self.second
        return result
    def sub(self) :
        result = self.first - self.second
        return result
    def times(self) :
        result = self.first * self.second
        return result
    def divide(self) :
        result = self.first / self.second
        return result

cal1 = FourCal(3, 8)
cal2 = FourCal(5, 5)

print(cal1.add())
print(cal1.sub())
print(cal1.times())
print(cal1.divide())

print(cal2.add())
print(cal2.sub())
print(cal2.times())
print(cal2.divide())


print()
#######################################
class MoreFourCal(FourCal): #하위 / 자식 클래스 
    def pow(self):
        result = self.first ** self.second
        return result


a = MoreFourCal(4, 2)
print("a.pow()", a.pow())

#########################################
#오버라이딩은 "상속'받는 관계에서만 가능
# 자식 객체의 오버라이드 함수에서 곧바로 부모 객체의 동일한 함수에 접근하는 방법?
# super() > 자식 클래스에서 부모 클래스의 함수에 접근할 때
class SafeFourCal(FourCal):
    def divide(self):
        if self.second ==0:
            return 0
        else:
            return super().divide()

b = SafeFourCal(4, 0)
c = SafeFourCal(4, 1)
print("b.divide()", b.divide())
print("c.divide()", c.divide())

    




