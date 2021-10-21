
# 클로저의 핵심 개념은 다음과 같습니다.

# - 외부 함수에서 내부 함수를 정의합니다.
# - 내부 함수에서 참조하는 변수는 내부 함수 객체에 같이 저장합니다.
# - 외부 함수는 내부 함수 객체를 리턴합니다.
# 가장 간단한 형태의 클로저는 다음과 같습니다.
# 외부함수인 outer가 호출될 때 내부 함수인 inner 함수의 객체를 생성하고 이를 리턴합니다.
# inner 함수 객체에는 enclosed functon local 영역의 num 값이 __closure__ 속성에 저장됩니다.

def outer(num):
    def inner():
        print(num)
    return inner

# outer 함수를 호출하면 생성된 inner 함수 객체의 주소가 리턴되며 이를 f1과 f2라는 변수가 바인딩합니다.
# 여러번 설명드리지만 여기서 중요한 점은 내부 함수에 대한 객체가 생성될 때 자신이 참조하는 num값인 3과 4를
# 내부 함수의 객체에 같이 저장하고 있다는 점입니다.

f1 = outer(3)
f2 = outer(4)
f1()
f2()


# closure vs. class

class Outer:
    def __init__(self, num):
        self.num = num
    def __call__(self):
        print(self.num)

# Outer 클래스에 대한 객체를 생성하고 이를 호출하면 됩니다.
# 참고로 클래스에 __call__ 메서드를 정의해두면 '객체( )'와 같이 사용할 때 __call__ 메서드가 호출됩니다.
# 사실 함수도 클래스의 객체이며 우리가 함수를 호출할 때 '함수이름( )'과 같이 사용할 수 있었던 이유가 바로 __call__ 메서드 덕분이었습니다.

f1 = Outer(3)
f2 = Outer(4)
f1()
f2()
