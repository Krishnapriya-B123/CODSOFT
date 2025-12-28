# Simple Calculator Program

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display available operations
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# User choice
choice = input("Enter your choice (1/2/3/4): ")

# Perform calculation and display result
if choice == "1":
    print("Result:", num1 + num2)

elif choice == "2":
    print("Result:", num1 - num2)

elif choice == "3":
    print("Result:", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid choice")
