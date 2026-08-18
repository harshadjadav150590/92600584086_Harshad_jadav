integer_value = 10
float_value = 25.5
string_value = "100"
boolean_value = True
complex_value = 3 + 4j

print("Integer:", integer_value, type(integer_value))
print("Float:", float_value, type(float_value))
print("String:", string_value, type(string_value))
print("Boolean:", boolean_value, type(boolean_value))
print("Complex:", complex_value, type(complex_value))

a = float(integer_value)
print("\nInteger to Float:", a)

b = str(integer_value)
print("Integer to String:", b)

c = int(string_value)
print("String to Integer:", c)

d = float(string_value)
print("String to Float:", d)

e = bool(integer_value)
print("Integer to Boolean:", e)

f = int(float_value)
print("Float to Integer:", f)
