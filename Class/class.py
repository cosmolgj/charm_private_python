class FourCal:
    lastname = "lee"   # 클래스 변수 (생성된 객체 모두에서 공유됨)

    def __init__(self, first, second):  # 생성자
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second


# self 는 호출한 객체를 자동으로 전달하는데 필요한 변수
# a = FourCal() 로 생성하였을 때
# a.add(1, 4) 와 FourCal.add(a, 1, 4) 가 동일

a = FourCal(4, 3)
print(a.first)
print(a.second)
print(type(a))
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())


# 클래스 상속 (기존 클래스가 라이브러리로 제공되거나 수정이 허용되지 않는 상황일 때)
class MoreFourCal(FourCal):
    def pow(self):
        return self.first ** self.second


b = MoreFourCal(2, 5) # 생성자 또한 상속되므로 객체 생성 시 초기값 부여
print("pow() is ", b.pow())


class SafeFourCal(FourCal):
    def div(self):   # overriding 함수 (부모클래스의 div 함수대신 호출)
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


c = SafeFourCal(4, 0)
print("SafeFourCal.div(c): ", c.div())




# 클래스를 선언합니다.
class Student:
    # 클래스 변수
    count = 0
    students = []

    # 클래스 함수
    @classmethod
    def print(cls):
        print("------ 학생 목록 ------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("------- ------- -------")

    # 인스턴스 함수
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + \
               self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format( \
            self.name, \
            self.get_sum(), \
            self.get_average())


# 학생 리스트를 선언합니다.
Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 98, 96, 98)
Student("구지연", 76, 96, 94, 90)
Student("나선주", 98, 92, 96, 92)
Student("윤아린", 95, 98, 98, 98)
Student("윤명월", 64, 88, 92, 92)
Student("김미화", 82, 86, 98, 88)
Student("김연화", 88, 74, 78, 92)
Student("박아현", 97, 92, 88, 95)
Student("서준서", 45, 52, 72, 78)

# 현재 생성된 학생을 모두 출력합니다.
Student.print()
