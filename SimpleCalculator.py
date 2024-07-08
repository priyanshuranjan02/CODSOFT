# Get user input for numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Get user input for operation
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = input("Enter choice (1/2/3/4): ")

# Perform calculation based on user choice
if operation == "1":
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result}")
elif operation == "2":
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result}")
elif operation == "3":
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result}")
elif operation == "4":
    if second_number == 0:
        print("Error: Division by zero")
    else:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result}")
else:
    print("Invalid operation choice")
