#미션: 클래스 선언 후 나의 핸드폰 정보를 저장하고 출력
#클래스는 프로그램 끝날 때 까지 살아있음
class Phone: 
    def __init__(self, name):
        self.name = name
        
    def setModel(self, x): #self는 지역변수(매개변수니까, 매개변수는 지역변수)
        self.model = input(f'{self.name} model input ')     
        #model = input() 이렇게 썼을 때 model은 지역변수
        
    def setColour(self, y):
       # self.colour = input(self.name, "colour input ")
       self.colour = input(f'{self.name} colour input ') 

    def setNumber(self, z):
        #self.number = input(self.name, "number input ")
        self.number = input(f'{self.name} number input ')
        
    def show(self):
        print(self.name ,self.model, self.colour, self.number)

'''        
myPhone = Phone("Dayeong")
myPhone.setModel()
myPhone.setColour()
myPhone.setNumber()

#출력 방법 1
print('model  ', myPhone.model)
print('color  ' , myPhone.colour)
print('number  ' , myPhone.number)
print(myPhone.name, myPhone.model, myPhone.colour, myPhone.number)

#출력 방법2
myPhone.show()
'''

#yourPhone = Phone('dayeong')
yourPhone = Phone(input('enter your name  '))
yourPhone.setModel(10)
yourPhone.setColour(20)
yourPhone.setNumber(30)
print(yourPhone.name, yourPhone.model, yourPhone.colour, yourPhone.number)


