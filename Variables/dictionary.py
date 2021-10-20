grade = {'kim': 10, 'choi': 90}

print(grade['kim'])
print(grade['choi'])

# key 값이 중복될 때 하나를 제외한 나머지는 무시
# key 에 리스트(mutable) 불가, 튜플(immutable) 가능

# dict_keys (cf. python 2.7 버전까지는 a.keys() 반환값이 리스트였다.
# 반환값이 필요할 경우에는 list(a.keys()) 사용)
# dict_keys, dict_values, dict_items 등은 기본적으로 반복구문 가능

a = {'name': 'chulsoo', 'phone': '01093982932', 'birth': '1129'}
print(a.keys())
print(list(a.keys()))

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))

# get value using key
print(a.get('name'))
print(a.get('phone'))

print(a.get('foo', 'nokey'))  # key 값이 없을 경우 미리 정해둔 default 값인 nokey 반환

# key 가 딕셔너리 안에 있는지 조사

print('name' in a)
print('email' in a)

# ===================================================================

# ===================================================================

# 딕셔너리 생성방법
# 1.
ice_cream_1 = {'merona':500, 'gugucon':1000}
print(ice_cream_1)

# 2. 키가 문자열일 경우
ice_cream_2 = dict(merona=500, gugucon=1000)
print(ice_cream_2)

# 3. 키와 값을 하나의 튜플로 저장하고 튜플들을 리스트로 저장후 딕셔너리 생성
ice_cream_3 = dict([('merona', 500), ('gugucon', 1000)])
print(ice_cream_3)



# setdefault     딕셔너리에 key 추가하면서 초기값 설정
data = {}
ret = data.setdefault('a', 0)   # key로 'a' 추가하고 value 0 설정, setdefault 는 현재 value 값 리턴
print(ret, data)

ret = data.setdefault('a', 1)   # 이미 key 가 있는 경우 setdefault 현재 value 값 리턴
print(ret, data)



# zip 으로 두개의 리스트 묶기
name = ['merona', 'gugucon']
price = [500, 1000]

z = zip(name, price)
print(list(z))



# zip 과 딕셔너리 관계
ice_cream_4 = dict(zip(name, price))
print(ice_cream_4)



# dictionary comprehension

name = ['merona', 'gugucon', 'bibibic']
price = [500, 1000, 600]

icecream = {k : v for k, v in zip(name, price) if v < 1000}
print(icecream)
