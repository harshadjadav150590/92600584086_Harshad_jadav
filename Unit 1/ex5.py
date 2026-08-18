numbers = [10, 20, 30, 40, 50]

print("Original List:")
print(numbers)


print("\nList Indexing:")
print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Last element:", numbers[-1])

print("\nList Slicing:")
print("First three elements:", numbers[0:3])
print("Middle elements:", numbers[1:4])
print("Last three elements:", numbers[2:])
print("Reverse list:", numbers[::-1])

print("\nList Manipulation:")

numbers.append(60)
print("After append:", numbers)

numbers.insert(2, 25)
print("After insert:", numbers)

numbers.remove(25)
print("After remove:", numbers)

numbers.pop()
print("After pop:", numbers)

numbers.sort()
print("After sorting:", numbers)

numbers.reverse()
print("After reverse:", numbers)

print("Length of list:", len(numbers))


print("\nList Comprehension:")

squares = [x * x for x in range(1, 6)]
print("Squares:", squares)

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", even_numbers)


odd_numbers = [x for x in range(1, 11) if x % 2 != 0]
print("Odd numbers:", odd_numbers)
