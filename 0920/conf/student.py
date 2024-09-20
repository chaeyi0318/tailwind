# 다른 모듈에 있는 클래스 가져오기
# conf 폴더 -> 패키지임
# 현재 같은 위치에 있는 base => .base
from .base import Person

# 학생 객체 -> 이름, 나이, 먹는다는 행위
class Student(Person):        # 상속할 부모 클래스를 () 안에 작성
    pass

s1 = Student('학생', 20)
print(s1.name)