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
