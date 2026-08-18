print("Welcome to the Python input/output program!")

name = input("Enter your name: ")

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

total = first_number + second_number

print("\nHello,", name)
print("The first number is:", first_number)
print("The second number is:", second_number)
print("The sum is:", total)
print(f"{name}, {first_number} + {second_number} = {total}")