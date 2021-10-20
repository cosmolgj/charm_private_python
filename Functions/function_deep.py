# 함수 이름은 함수타입의 객체를 가리키는 변수
# __call__ 메소드는 호출 메소드인대ㅔ 객체를 생성한 후 () 만 붙여주면 자동으로 __call__ 메소드 호출된다
# 객체가 생성될 때 생성자인 __init__ 이 자동으로 호출되는것과 비슷

class Func:
    def __init__(self):
        print("initialized")

    def __call__(self):
        print("called")


f = Func()  # __init__ 호출됨
f()  # __call__ 호출됨


# positional variable argument (*args)
# 함수 호출시 args 라는 변수는 여러개의 입력에 대해 튜플로 저장한 후 이 튜플 객체를 바인딩

def foo(*args):
    print(args)


foo(1, 2, 3)
foo(1, 2, 3, 4)


# keyword variable arguments (**kwargs)
def foo2(**kwargs):
    print(kwargs)


foo2(a=1, b=2, c=3)


def foo3(*args, **kwargs):
    print(args)
    print(kwargs)


foo3(1, 2, 3, a=1, b=2, c=3)


# 함수 인자로 리스트/튜플 전달하기

def foo4(a, b, c):
    print(a, b, c)

data = [1, 2, 3]
foo4(*data)
