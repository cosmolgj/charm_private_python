
# file creation

f = open("new_file.txt", 'w')   # 'r' 읽기모드, 'w' 쓰기모드, 'a' 추가모드
f.close()

# 파일경로
# C:/cosmolgj/new_file.txt
# C:\\cosmolgj\\new_file.txt
# r"C:\cosmolgj\new_file.txt"

# write 함수
f = open("new_file.txt", 'w')
for i in range(1, 11):
    data = "%dth line.\n" % i
    f.write(data)
f.close()

# readline 함수 (한줄씩 읽어들이기)
f = open("new_file.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("new_file.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line, end='\r')
f.close()

# readlines 함수 (파일의 모든 줄 읽어서 각각의 줄을 요소로 갖는 리스트로 리턴)
print("{0:=^30}".format(" readlines function "))
f = open("new_file.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()    # 줄바꿈 ('\n') 제거
    print(line)
f.close()

# read 함수 (내용 전체를 문자열로 리턴)
print("{0:=^30}".format(" read function "))
f = open("new_file.txt", 'r')
data = f.read()
print(data)
f.close()

# append to write
f = open("new_file.txt", 'a')
for i in range(11, 21):
    data = "%dth line.\n" % i
    f.write(data)
f.close()


# open to use with. with 블록을 벗어나는 순간 객체 f 가 자동으로 close
with open("new_file.txt", 'r') as f:
    f.read()


