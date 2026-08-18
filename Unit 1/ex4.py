
text = "Python Programming"

print("Original String:")
print(text)

print("\nString Indexing:")
print("First character:", text[0])
print("Last character:", text[-1])


print("\nString Slicing:")
print("First 6 characters:", text[0:6])
print("Programming:", text[7:18])
print("Every second character:", text[::2])
print("Reverse string:", text[::-1])

name = "Rahul"
age = 20

print("\nString Formatting:")
print(f"My name is {name} and I am {age} years old.")

print("\nBuilt-in String Functions:")

print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Capitalize:", text.capitalize())
print("Title:", text.title())
print("Replace:", text.replace("Python", "Java"))
print("Find 'Programming':", text.find("Programming"))
print("Count of 'm':", text.count("m"))

sample = "   Hello Python   "
print("Before strip:", sample)
print("After strip:", sample.strip())

words = text.split()
print("After split:", words)

