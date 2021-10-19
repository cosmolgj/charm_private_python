
def add(a, b):
    return a + b


def sub(a, b):
    return a - b

PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)


if __name__ == "__main__":    # 실행 파일로서의 역할로는 print 함수
    print(add(1, 5))
    print(sub(8, 2))

