# outer()  외부함수   inner()  내부함수

def outer():
    def inner():
        print("inner")

    return inner


f = outer()
f()


# 위 코드가 수행되는 과정을 그림으로 그려보면 다음과 같습니다. 개념이 어려울 때 그림으로 그려보고 이해하는 것이 좋습니다.
# 앞서 함수 이름은 함수 객체를 바인딩하는 변수라고 했습니다. 즉, outer는 외부 함수 객체를 바인딩합니다.
# 함수 이름에 ( ) 를 붙이면 해당 함수 코드가 실행되었죠?
# outer 함수가 실행되면 outer에 정의된 코드가 실행되는데 이때 inner 함수가 정의되고 inner라는 변수가 내부 함수 객체를 바인딩합니다.
# 마지막으로 inner가 가리키는 함수 객체를 리턴하고 그 값을 Global 영역의 변수 f가 바인딩합니다.
# 따라서 f는 print("inner")라는 코드의 함수 객체입니다. 그러므로 f( )와 같은 표현을 통해 f 함수를 호출하면 화면에 'inner'가 출력되는 겁니다.


# enclosed function locals

def outer2():
    num = 3

    def inner():
        print(num)

    return inner


f = outer2()
f()

# 내부 함수 inner에서 num 값을 참조하고 있습니다. 파이썬에서 변수를 참조하면 LEGB 순으로 탐색했지요?
# 내부 함수 inner에는 num이 없으므로 Enclosed function locals 영역을 탐색하는데 해당 영역이 바로 내부 함수 밖이면서 Global 영역 안쪽을 의미합니다.
# 즉, 아래의 예제에서 num이 바로 Enclosed function locals 영역에 있는 변수입니다.
# 내부 함수 객체는 함수 객체가 생성될 때 자신이 참조하는 Enclosed function locals 영역의 변수를 자신의 객체 안에 저장합니다.

print(f.__closure__[0].cell_contents)   # 변수 num 의 값을 가지고 있음

# 현재 f라는 변수가 바인딩하는 function 타입의 객체는 __closure__라는 속성을 갖고 있습니다.
# 해당 속성은 튜플 타입의 객체를 바인딩합니다.
# 앞의 예에서는 Enclosed function locals 영역의 변수가 하나 이므로 튜플의 개수는 1개 입니다.
# 튜플의 0번은 cell 타입의 객체를 바인딩하는데 이 cell 타입의 객체의 'cell_contents' 속성에 3이라는 값이 저장되어 있는 겁니다.

print(type(f.__closure__))     # tuple
print(type(f.__closure__[0]))  # cell
print(dir(f.__closure__[0]))

def outer3(num):
    def inner():
        print(num)
    return inner
# outer3 의 인자인 num은 로컬변수. 내부함수인 inner 입장에서는 enclosed function locals 영역에 있는 변수