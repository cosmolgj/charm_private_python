def add(a, b):
    return a + b


res = add(b=5, a=3)
print(res)


# 여러개의 입력 값 받는 함수
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result


res = add_many(2, 4, 5, 6)
print(res)


def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result


res = add_mul('add', 1, 2, 3, 4, 5)
print("add_mul(add): ", res)
res = add_mul('mul', 1, 2, 3, 4, 5)
print("add_mul(mul): ", res)


# 키워드 파라미터 kwargs (= keyword arguments)
# 매개변수 앞에 ** 를 붙이면 매개변수 kwargs 는 딕셔너리가 되고 모든 key = value 형태의 결과값이 딕셔너리에 저장됨
def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(a=1)
print_kwargs(name='kim', age=3)


# 매개변수에 초기값 설정
# 초기화 시키고 싶은 매개변수를 항상 뒤부터 위치시켜야 함

def say_myself(name, old, man=True):
    print("my name is %s." % name)
    print("my age is %d." % old)
    if man:
        print("man")
    else:
        print("woman")


say_myself("namil park", 32)
say_myself("namil park", 32, True)

# 람다(lambda) 함수
add = lambda a, b: a + b
res = add(3, 5)
print(res)





"""
# 매개변수로 받은 함수를 10번 호출하는 함수
def call_10_times(func):
    for i in range(10):
        func()

# 간단한 출력하는 함수
def print_hello():
    print("안녕하세요")

# 조합하기
call_10_times(print_hello)


# 함수 데코레이터를 생성합니다.
def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper

# 데코레이터를 붙여 함수를 만듭니다.
@test
def hello():
    print("hello")

# 함수를 호출합니다.
hello()
"""
