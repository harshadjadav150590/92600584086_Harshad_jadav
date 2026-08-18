print("MUTABLE OBJECT")
print("--------------")

numbers = [10, 20, 30]

print("Original List:", numbers)
print("ID before change:", id(numbers))

numbers.append(40)

print("Modified List:", numbers)
print("ID after change:", id(numbers))


print("\nIMMUTABLE OBJECT")
print("----------------")

x = 10

print("Original value:", x)
print("ID before change:", id(x))

x = x + 5

print("Modified value:", x)
print("ID after change:", id(x))


print("\nSTRING - IMMUTABLE")

name = "Python"

print("Original String:", name)
print("ID before change:", id(name))

name = name + " Programming"

print("Modified String:", name)
print("ID after change:", id(name))

