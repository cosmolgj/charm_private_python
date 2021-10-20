# 튜플 요소를 지우거나 변경하려고 할때 모두 에러!!

# indexing


# slicing

# add

# multiply

# get lenth


# tuple packing
# a와 같이 여러개의 값을 콤마로 구분해도 튜플로 인식. 이를 튜플 패킹이라 함

a = 1, 2
b = (1, 2)

print(a, type(a))
print(b, type(b))


# tuple unpacking
data = (1, 2, 3)
n1, n2, n3 = data

scores = (1, 2, 3, 4, 5, 6)
low, *others, high = scores
print(others)


# tuple unpacking 과 함수 호출
def hap(num1, num2, num3, num4):
    return num1+num2+num3+num4

scores = (1, 2, 3, 4)
result = hap(*scores)
print(result)


# namedtuple


class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price


mybook = Book("auto-buying using python", 27000)
print(mybook.title, mybook.price)

# 튜플은 immutable 타입이라 변경할 필요없는 데이터 저장에는 효과적이나 딕셔너리와 비교했을 때
# 값에 대한 라벨(정보)가 없다
# 이에 namedtuple 은 클래스처럼 객체를 생성할 수 있고 딕셔너리처럼 값에 대한 라벨을 부여할 수 있다

from collections import namedtuple
Book = namedtuple('Book', ['title', 'price'])
mybook2 = Book('auto-buying using python', 27000)
print(mybook2.title, mybook2.price)


# namedtuple unpacking  함수의 인자들이 하나의 튜플 객체로 표현된 경우 tuple unpacking 사용 가능
def print_book(title, price):
    print(title, price)

print_book(*mybook2)
