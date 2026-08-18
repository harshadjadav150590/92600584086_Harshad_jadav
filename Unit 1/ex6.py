numbers = (10, 20, 30, 40, 50, 20)

print("TUPLE OPERATIONS")


print("Original Tuple:", numbers)


print("First element:", numbers[0])
print("Last element:", numbers[-1])

print("Sliced Tuple:", numbers[1:4])

print("Length of Tuple:", len(numbers))

print("Count of 20:", numbers.count(20))

print("Index of 30:", numbers.index(30))

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("\nSET OPERATIONS")
print("-------------")

print("Set 1:", set1)
print("Set 2:", set2)

set1.add(50)
print("After adding 50:", set1)


set1.remove(50)
print("After removing 50:", set1)

print("Union:", set1.union(set2))

print("Intersection:", set1.intersection(set2))

print("Set1 - Set2:", set1.difference(set2))

print("Set2 - Set1:", set2.difference(set1))

