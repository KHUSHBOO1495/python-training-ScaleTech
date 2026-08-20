from operations import add, subtract, multiply, divide

while True:
    print("\n=== Simple Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option:")
    if choice == '5':
        print("Goodbye!")
        break
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        try:
            print(f"Result: {divide(num1, num2)}")
        except ValueError as error:
            print("Error:", error)
