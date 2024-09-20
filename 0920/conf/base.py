class Person:
    # class 변수
    population = 0
    
    # 생성자 함수
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        # 인스턴스가 생성 될 때마다 population 1 증가
        Person.increase()
        
    # 인스턴스 메서드
    def eat(self):
        print('밥을 먹는다.')
    
    # 클래스 메서드    
    @classmethod
    def increase(cls):
        cls.population += 1
        

# 인스턴스
p1 = Person('사람', 20)
p2 = Person('인간', 40)

print(p1.population, p2.population)

print(p1)       # Person 클래스의 인스턴스 p1
p1.eat()        # 인스턴스가 호출 할 수 있는 메서드
p2.eat()        # 모든 Person 클래스의 인스턴스는 eat 메서드 호출 가능

print(p1.name)