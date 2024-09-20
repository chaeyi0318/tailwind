# conf 패키지에 있는 2개의 클래스 모두 가져오기
from conf.student import Student
from conf.teacher import Teacher



class Course:
    def __init__(self):
        self.students = []
        self.teacher = None
        
c1 = Course()
print(c1.students, c1.teacher)

s1 = Student('학생', 20)
t1 = Teacher('선생', 50)
c1.teacher = t1

print(c1.students, c1.teacher)
c1.teacher.eat()
print(c1.teacher.name)