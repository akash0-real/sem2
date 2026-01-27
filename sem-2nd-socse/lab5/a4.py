def list_operations():
    """
    Performs various operations on a list, including insert, delete, find, sort, and reverse.
    """

    my_list = []

    while True:
        print("\nList Operations Menu:")
        print("1. Insert element")
        print("2. Delete element")
        print("3. Find element")
        print("4. Sort list")
        print("5. Reverse list")
        print("6. Print list")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            element = input("Enter element to insert: ")
            index = input("Enter index (leave blank for append): ")
            if index:
                try:
                    index = int(index)
                    my_list.insert(index, element)
                except ValueError:
                    print("Invalid index input.")
                except IndexError:
                    print("Index out of range.")
            else:
                my_list.append(element)

        elif choice == "2":
            element = input("Enter element to delete: ")
            try:
                my_list.remove(element)
            except ValueError:
                print("Element not found.")

        elif choice == "3":
            element = input("Enter element to find: ")
            if element in my_list:
                print(f"{element} found at index {my_list.index(element)}")
            else:
                print("Element not found.")

        elif choice == "4":
            my_list.sort()
            print("List sorted.")

        elif choice == "5":
            my_list.reverse()
            print("List reversed.")

        elif choice == "6":
            print("Current list:", my_list)

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

sal= list_operations()
