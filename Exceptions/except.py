# 1. try, except
'''
try:
    pass
except:
    pass
'''
# 2. 발생오류만 포함한 except
'''
try:
    pass
except 발생오류:
    pass
'''
# 3. 발생오류와 오류 메시지 변수까지 포함한 except
'''
try:
    pass
except 발생오류 as 오류 메시지 변수:
    pass
'''

# 4. try ...finally
# finally 절은 예외발생 여부에 상관없이 항상 수행


# 5. 여러개의 오류처리하기
'''
try:
except 발생오류1:
except 발생오류2:
    ...
'''


# 6. try... except...else

# 7. 오류 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError  # 상속 클래스에서 fly 함수를 꼭 구현해야 된다


class Eagle(Bird):
    pass


# eagle = Eagle()
# eagle.fly()

import Exceptions


class MyError(Exception):
    def __str__(self):          # except 에러 처리 시 print(e) 처럼 오류 메시지 출력할 경우 호출되는 메서드
        return "not permitted nick"


def say_nick(nick):
    if nick == 'fool':
        raise MyError()
    print(nick)


try:
    say_nick('angel')
    say_nick('fool')
except MyError:
    print("not permitted nick")


try:
    say_nick('cow')
    say_nick('fool')
except MyError as e:
    print(e)






'''
try:
    # 숫자로 변환합니다.
    number_input_a = int(input("정수 입력> "))
    # 출력합니다.
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except Exception as exception:
    # 예외 객체를 출력해봅니다.
    print("type(exception):", type(exception))
    print("exception:", exception)
'''
