try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Sum:", num1 + num2)

except ValueError:
    print("Error: Both inputs must be numbers.")
