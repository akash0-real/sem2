def find_largest():
    numbers = []
    print("Enter 5 numbers:")

    for i in range(5):
        try:
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            return

    largest = max(numbers)

    print(f"The largest number among {numbers} is {largest}.")

print(find_largest())
