############################################################
# method 1 for formatting
# %s string, %c character, %d integer, %f floating-point, %o octal, %x hexadecimal

string_a = "I eat %d apples." % 3
print(string_a)

string_b = "I eat %s apples." % "five"
print(string_b)

number = 7
string_c = "I eat %d apples." % number
print(string_c)

day = "four"
string_d = "I ate %d apples. so i was sick for %s days." % (number, day)
print(string_d)

############################################################
# method 2 for formatting

string_e = "I eat {0} apples.".format(3)
print(string_e)

string_f = "I eat {0} apples.".format("five")
print(string_f)

string_g = "I eat {} apples.".format(number)
print(string_g)

string_h = "I eat {0} apples. So i was sick for {1} days.".format(number, day)
print(string_h)

# left sorting

string_i = "{0:<10}".format("hi")
print(string_i)

# right sorting

string_j = "{0:>10}".format("hi")
print(string_j)

# centeral sorting

string_k = "{0:^10}".format("hi")
print(string_k)

# fill empty space

string_l = "{0:=^20}".format(" hi ")
print(string_l)

string_m = "{0:=<20}".format(" hi ")
print(string_m)

# present floating-point

a = 3.425489823
print("{0:0.4f}".format(a))

print("{0:10.4f}".format(a))


############################################################
# method 3 for formatting (f formatting)

name = 'Chulsoo Kim'
age = 34

print(f"my name is {name}. age is {age}.")

d = {'name':'Chulsoo Kim', 'age':34}
print(f"my name is {d['name']}. age is {d['age']}")

print(f"{'hi':<20}")    # left sorting with f formatting
print(f"{'hi':>20}")    # right sorting with f formatting
print(f"{'hi':^20}")    # central sorting with f formatting

print(f"{' hi ':=^20}")


############################################################
"""
string_a = "{}".format(10)

print(string_a)
print(type(string_a))

format_a = "{} won".format(5000)
format_b = "make {} won".format(5000)
format_c = "{} {} {}".format(100, 200, 300)
format_d = "{} {} {}".format(1, "string", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)

output_a = "{:d}".format(52)
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)
print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)

output_f = "{:+d}".format(52)
output_g = "{:+d}".format(-52)
output_h = "{: d}".format(52)
output_i = "{: d}".format(-52)
print(output_f)
print(output_g)
print(output_h)
print(output_i)

output_j = "{:+5d}".format(52)
output_k = "{:+5d}".format(-52)
output_l = "{:=+5d}".format(52)
output_m = "{:=+5d}".format(-52)
output_n = "{:+05d}".format(52)
output_o = "{:+05d}".format(-52)
print(output_j)
print(output_k)
print(output_l)
print(output_m)
print(output_n)
print(output_o)

output_p = "{:f}".format(52.273)
output_q = "{:15f}".format(52.273)
output_r = "{:+15f}".format(52.273)
output_s = "{:+015f}".format(52.273)
print(output_p)
print(output_q)
print(output_r)
print(output_s)

output_t = "{:15.3f}".format(52.273)
output_u = "{:15.2f}".format(52.273)
output_v = "{:15.1f}".format(52.273)
print(output_t)
print(output_u)
print(output_v)

output_w = 52.0
output_x = "{:g}".format(output_w)
print(output_w)
print(output_x)
"""