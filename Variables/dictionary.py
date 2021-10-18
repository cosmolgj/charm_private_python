
grade = {'kim': 10, 'choi': 90}

print(grade['kim'])
print(grade['choi'])

# key 값이 중복될 때 하나를 제외한 나머지는 무시
# key 에 리스트(mutable) 불가, 튜플(immutable) 가능

# dict_keys (cf. python 2.7 버전까지는 a.keys() 반환값이 리스트였다.
# 반환값이 필요할 경우에는 list(a.keys()) 사용)
# dict_keys, dict_values, dict_items 등은 기본적으로 반복구문 가능

a = {'name':'chulsoo', 'phone':'01093982932', 'birth':'1129'}
print(a.keys())
print(list(a.keys()))

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))

# get value using key
print(a.get('name'))
print(a.get('phone'))

print(a.get('foo', 'nokey'))   #  key 값이 없을 경우 미리 정해둔 default 값인 nokey 반환

# key 가 딕셔너리 안에 있는지 조사

print('name' in a)
print('email' in a)
