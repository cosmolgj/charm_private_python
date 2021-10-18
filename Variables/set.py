
# 집합 자료형의 특징
# 1. 중복을 허용하지 않는다
# 2. 순서가 없다 (unordered)

s1 = set([1, 2, 3])
print(s1)

s2 = set('hello')
print(s2)    # 중복된 요소 생략

# set 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환
print(list(s1))
print(tuple(s1))

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

# 값 1개 추가
s1.add(7)
print(s1)

# 값 여러개 추가
s1.update([7, 8, 9])
print(s1)

# 특정 값 제거
s1.remove(7)
print(s1)
