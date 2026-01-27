
def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Floor Divide")
        print("6. Power")
        print("7. Modulus")
        print("8. Exit")
        
      
        choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

        if choice == '8':
            print("Exiting the calculator.")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        
        if choice == '1':
            print(f"The result is: {num1 + num2}")
        elif choice == '2':
            print(f"The result is: {num1 - num2}")
        elif choice == '3':
            print(f"The result is: {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("Error! Division by zero.")
            else:
                print(f"The result is: {num1 / num2}")
        elif choice == '5':
            if num2 == 0:
                print("Error! Division by zero.")
            else:
                print(f"The result is: {num1 // num2}")
        elif choice == '6':
            print(f"The result is: {num1 ** num2}")
        elif choice == '7':
            print(f"The result is: {num1 % num2}")
        else:
            print("Invalid choice! Please select a valid operation.")

print(calculator())
