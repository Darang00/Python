class Animal:
    def __init__(self, name, action, feed):
        print("Animal")
        self.name = name
        self.action = action
        self.feed = feed

    def get_name(self):
        print(f'나는 {self.name} 입니다.')

    def get_move(self):
        print(f'{self.action} 합니다.')

    def get_eat(self):
        print(f'{self.feed}를 먹습니다')

class Dog(Animal):
    def __init__(self, name, action, feed, bark):
        print("Dog")

        super().__init__(name, action, feed)

        self.bark = bark

    def get_bark(self):
        print(f'{self.bark} 하고 짖습니다.')

dog = Dog("푸들", "달리기", "뼈다귀", "멍멍")
dog.get_name()
dog.get_move()
dog.get_eat()
dog.get_bark()
        
