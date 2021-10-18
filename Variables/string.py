
# 큰 따옴표
print("hello")
# 작은 따옴표
print('hello')

print("'hello'")

print('"hello"')

print("I think \"hello\"")

# 여러줄 문자열 대입
multiline_a = '''
Life is too short
you need python
'''

multiline_b = """
Life is too short
you need python
"""
print(multiline_a)
print(multiline_b)

print("hello" * 3)

print(3 * "hello")

# indexing

print("hello"[0])
print("hello"[1])
print("hello"[2])
print("hello"[3])
print("hello"[4])


# slicing

print('"hello"[1:4]: ' + "hello"[1:4])

print("hello"[1:])
print("hello"[:3])

# get length

print(len("hello"))
