
string = input("input hello: ")

print(string)
print(type(string))

string2 = input("input number: ")
print(string2)
print(type(string2))

# convert to int using int function
string_a = input("input num_A > ")
int_a = int(string_a)

string_b = input("input num_B > ")
int_b = int(string_b)

print("string: ", string_a + string_b)
print("number: ", int_a + int_b)

# convert to string from int

output_a = str(52)
output_b = str(52.273)

print(type(output_a), output_a)
print(type(output_b), output_b)
