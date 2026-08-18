def add(a, b):
    return a + b


print("1. Positional Arguments")
print("Addition:", add(10, 20))


def student(name, age):
    print("Name:", name)
    print("Age:", age)


print("\n2. Keyword Arguments")
student(age=20, name="Chandan")


def greet(name, message="Good Morning"):
    print(message, name)


print("\n3. Default Argument")
greet("Chandan")
greet("Amit", "Good Evening")


def total(*numbers):
    result = 0

    for num in numbers:
        result = result + num

    return result


print("\n4. Variable-Length Arguments")
print("Total:", total(10, 20))
print("Total:", total(10, 20, 30, 40))


def display_details(**details):
    for key, value in details.items():
        print(key, ":", value)


print("\n5. Variable-Length Keyword Arguments")
display_details(name="Chandan", age=20, course="MCA")
