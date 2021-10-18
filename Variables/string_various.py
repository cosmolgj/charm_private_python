
# count character
string = "hobby"
print(string.count('b'))

string = "python is the best choice"
print(string.find('b'))
print(string.find('k'))  # not find character
print(string.index('b'))
# print(string.index('k'))  # find error

# join string
print(", ".join("abcd"))
print(", ".join(['a', 'b', 'c', 'd']))

print(string.upper())
print(string.lower())

# strip function
input_a = """
     hello    
string function
"""

print(input_a)
print(input_a.strip())

# replace
print(string.replace("python", "C++"))


# isalnum, isalpha, isidentifier, isdecimal, isdigit, isspace, islower, isupper

output_a = "hellohello".find("hello")
print(output_a)

output_b = "hellohello".rfind("hello")
print(output_b)

print("hel" in "hello")

# split

a = "10 20 30 40 50".split(" ")
print(a)

a = "Life is too short"
print(a.split())

a = "a:b:c:d"
print(a.split(":"))
