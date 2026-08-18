student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA",
    "marks": 85
}

print("Original Dictionary:")
print(student)


print("\nAccessing Dictionary Values:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])


print("\nUsing get() method:")
print("Marks:", student.get("marks"))


print("\nDictionary Keys:")
print(student.keys())


print("\nDictionary Values:")
print(student.values())


print("\nDictionary Items:")
print(student.items())


student.update({"marks": 90, "city": "Patna"})
print("\nAfter update():")
print(student)


student.pop("city")
print("\nAfter pop():")
print(student)


print("\nLength of Dictionary:")
print(len(student))


print("\nIteration through Keys:")
for key in student:
    print(key)


print("\nIteration through Values:")
for value in student.values():
    print(value)

print("\nIteration through Key-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

