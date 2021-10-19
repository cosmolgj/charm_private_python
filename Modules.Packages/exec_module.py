import module
from module import add, sub  # 2개 함수만 import
from module import *         # module 의 모든 함수 import

print(module.add(2, 8))

print(module.sub(7, 4))

print(add(3, 4))

print(sub(9, 2))

# module 을 위치 상관없이 불러들이기 위한 방법
# 1. sys.path 에 모듈 경로 추가
#    import sys
#    sys.path.append(경로명)
# 2. PYTHONPATH 환경 변수 사용
#    set PYTHONPATH=C:\경로명


# 모듈을 읽어 들입니다.
import datetime

# 현재 시각을 구하고 출력하기
print("# 현재 시각 출력하기")
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

# 시간 출력 방법
print("# 시간을 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
now.month,\
now.day,\
now.hour,\
now.minute,\
now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(output_a)
print(output_b)
print(output_c)
print()
