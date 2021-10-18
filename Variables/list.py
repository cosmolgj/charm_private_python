
# slicing

a = [1, 2, 3, 4, 5]

print(a[0:2])

# add

a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)

# length

print("length of a list: ", len(a))

# modify value of list

a[2] = 9
print(a)

# delete value of list
del a[2]
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

# append

a.append(7)
print(a)

a.append([5, 6])
print(a)

# sort

a = [5, 3, 2, 4, 1]
a.sort()
print(a)

# reverse

a.reverse()
print(a)

# insertion

a.insert(0, 3)
print(a)


# remove

a.remove(3)
print(a)

# pop. 맨 마지막 요소 돌려주고 삭제

a.pop()
print(a)


a.extend([6, 7, 8])
print(a)
