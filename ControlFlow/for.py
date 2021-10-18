
a = ['one', 'two', 'three']
for i in a:
    print(i)


b = [(1, 2), (3, 4), (5, 6)]
for (first, last) in b:
    print(first + last)

marks = [90, 26, 67, 48, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("Congrats! %dth student. You're passed." % number)

for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("Congrats! %dth student. You're passed." % (number+1))

# list comprehension

a = [1, 2, 3, 4]

result = []
for num in a:
    result.append(num*3)
print(result)

result = []
result = [num * 3 for num in a]
print(result)

result = []
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# 구구단
result = [x*y for x in range(2, 10)
          for y in range(1, 10)]
print(result)