class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(f'제 이름은 {self.name} 입니다')

    def get_age(self):
        print(f'제 나이는 {self.age} 입니다')

'''
px = Person("이순신", 20)
py = Person("김유신", 40)

px.get_name()
px.get_age()

py.get_name()
py.get_age()
'''

class Student(Person):
    def __init__(self, name, age, gpa):
        print("soderived class")

        super().__init__(name, age)
        
        #self.name = name
        #self.age = age
        self.gpa = gpa

    def get_gpa(self):
        print(f'제 학점은 {self.gpa} 입니다')


std = Student("짱구", 23, 4.5)
std.get_name()
std.get_age()
std.get_gpa()


#오버라이딩은 "상속'받는 관계에서만 가능
# 자식 객체의 오버라이드 함수에서 곧바로 부모 객체의 동일한 함수에 접근하는 방법?
# super() > 자식 클래스에서 부모 클래스의 함수에 접근할 때
