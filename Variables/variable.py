
# 리스트 참조하는 새로운 변수할당
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))

# 리스트 복사
a = [1, 2, 3]
b = a[:]     # list copy 1
a[1] = 4
print(a)
print(b)

from copy import copy
b = copy(a)   # list copy 2
b[1] = 7
print(a)
print(b)

b = a.copy()   #  리스트의 자체 함수
print(a)
print(b)

"""
def print_n_times(n, *values):
    # n번 반복합니다.
    for i in range(n):
        # values는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        # 단순한 줄바꿈
        print()

# 함수를 호출합니다.
print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")
"""