# sys  (파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어)

import sys

# 명령행 인수전달 (sys.argv)
print(sys.argv)

# 스크립트 강제종료  (sys.exit)
# sys.exit()

# 모듈 저장 위치  (sys.path)

# pickle  (객체의 형태를 그대로 유지하며넛 파일에 저장하고 불러올 수 있게 하는 모듈)

import pickle

f = open("pickle_test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

f = open("pickle_test.txt", 'rb')
data = pickle.load(f)
print(data)

# os   (환경변수나 디렉터리, 파일 등의 OS 자원을 제어)

# 내 시스템의 환경 변수값 (os.environ)
import os
print(os.environ)

# 디렉터리 위치 변경 (os.chdir)
# os.chdir("C:\Windows")

# 디렉터리 위치 받기 (os.getcwd)
os.getcwd()

# 시스템 명령어 호출  (os.system)
os.system("dir")

# 시스템 명령어의 결과값 돌려받기 (os.popen)
f = os.popen("dir")
print(f.read())


# shutil   (파일 복사)

import shutil
# shutil.copy("src.txt", "dst.txt")

# glob   (특정 디렉토리에 있는 파일 목록 만들기)
import glob
glob.glob("C:/*")


# time   (시간과 관련된 모듈)

# time.time  (현재 시간을 실수 형태로 돌려주는 함수)
import time
print(time.time())

# time.localtime   (실수값을 사용해서 연도, 월, 시, 분, 초 변환)
print(time.localtime(time.time()))

# time.asctime    (time.localtime 에 의해 반환된 류플 형태의 값을 인수로 받아 날짜와 시간을 보기 쉬운 형태로 변경)
print(time.asctime(time.localtime(time.time())))

# time.ctime   (현재 시간)
print(time.ctime())

# time.strftime   (시간에 관련된 여러 포맷 제공)
# time.strftime('to show format code', time.localtime(time.time()))
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))


# time.sleep   (일정한 시간간격 정지)

# random
import random
print(random.random())
print(random.randint(1, 10))
print(random.randint(1, 55))
